import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.core.database import Base
from app.core.models import Customer, Product
from app.features.bloquear_estoque_negativo.service import (  # noqa: F401 registra o listener
    InsufficientStockError,
)


@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    with Session(engine) as db:
        yield db


# ---------- Caminho feliz ----------

def test_compra_dentro_do_estoque_nao_gera_erro(session):
    produto = Product(name="Arroz", description="d", category="c", price=10.0, stock=10)
    session.add(produto)
    session.commit()

    produto.stock -= 5
    session.commit()
    assert produto.stock == 5


def test_estoque_chegando_exatamente_a_zero_e_permitido(session):
    """Zero não é negativo — a regra não deve bloquear esse caso limite."""
    produto = Product(name="Feijão", description="d", category="c", price=8.0, stock=5)
    session.add(produto)
    session.commit()

    produto.stock -= 5
    session.commit()  # não deve lançar
    assert produto.stock == 0


def test_reposicao_de_estoque_e_permitida(session):
    """Aumentar o estoque (reabastecimento) nunca deve ser bloqueado."""
    produto = Product(name="Sal", description="d", category="c", price=3.0, stock=0)
    session.add(produto)
    session.commit()

    produto.stock += 20
    session.commit()  # não deve lançar
    assert produto.stock == 20


# ---------- Bloqueio ----------

def test_compra_acima_do_estoque_e_rejeitada(session):
    produto = Product(name="Feijão", description="d", category="c", price=8.0, stock=3)
    session.add(produto)
    session.commit()

    produto.stock -= 4  # deixaria em -1
    with pytest.raises(InsufficientStockError):
        session.commit()


def test_estoque_ja_zerado_nao_pode_ser_reduzido(session):
    """Estoque vazio (0) tentando reduzir mais ainda deve ser bloqueado."""
    produto = Product(name="Óleo", description="d", category="c", price=12.0, stock=0)
    session.add(produto)
    session.commit()

    produto.stock -= 1
    with pytest.raises(InsufficientStockError):
        session.commit()


def test_mensagem_informa_o_problema(session):
    produto = Product(name="Açúcar", description="d", category="c", price=5.0, stock=2)
    session.add(produto)
    session.commit()

    produto.stock -= 5
    with pytest.raises(InsufficientStockError) as exc_info:
        session.commit()
    assert "Açúcar" in str(exc_info.value)
    assert "-3" in str(exc_info.value)


def test_reducao_muito_maior_que_o_estoque_tambem_e_bloqueada(session):
    """Garante que a regra não depende da magnitude do déficit."""
    produto = Product(name="Café", description="d", category="c", price=15.0, stock=1)
    session.add(produto)
    session.commit()

    produto.stock -= 1000
    with pytest.raises(InsufficientStockError):
        session.commit()


# ---------- Múltiplos objetos no mesmo flush ----------

def test_um_produto_negativo_entre_varios_bloqueia_o_commit_inteiro(session):
    """
    Se dois produtos forem alterados no mesmo commit e só um ficar
    negativo, o commit inteiro deve falhar (atomicidade).
    """
    ok = Product(name="Macarrão", description="d", category="c", price=4.0, stock=10)
    ruim = Product(name="Molho", description="d", category="c", price=6.0, stock=2)
    session.add_all([ok, ruim])
    session.commit()

    ok.stock -= 3       # ainda válido (vai pra 7)
    ruim.stock -= 5      # inválido (vai pra -3)

    with pytest.raises(InsufficientStockError):
        session.commit()

    session.rollback()
    session.refresh(ok)
    session.refresh(ruim)
    # nenhuma das duas mudanças foi persistida
    assert ok.stock == 10
    assert ruim.stock == 2


def test_dois_produtos_validos_no_mesmo_commit_nao_bloqueia(session):
    a = Product(name="Leite", description="d", category="c", price=4.5, stock=10)
    b = Product(name="Pão", description="d", category="c", price=2.0, stock=8)
    session.add_all([a, b])
    session.commit()

    a.stock -= 2
    b.stock -= 3
    session.commit()  # não deve lançar

    assert a.stock == 8
    assert b.stock == 5


# ---------- Recuperação após erro ----------

def test_apos_erro_a_sessao_permite_nova_operacao_valida_depois_do_rollback(session):
    """
    Garante que o bloqueio não deixa a sessão num estado inutilizável:
    após rollback, uma nova operação válida deve funcionar normalmente.
    """
    produto = Product(name="Manteiga", description="d", category="c", price=9.0, stock=2)
    session.add(produto)
    session.commit()

    produto.stock -= 5
    with pytest.raises(InsufficientStockError):
        session.commit()

    session.rollback()
    session.refresh(produto)
    assert produto.stock == 2  # valor original preservado

    produto.stock -= 1  # operação válida, depois do erro anterior
    session.commit()
    assert produto.stock == 1


# ---------- Objetos que não são Product ----------

def test_alterar_outro_modelo_nao_dispara_a_regra(session):
    """
    O listener deve ignorar objetos que não são Product, mesmo que
    estejam 'dirty' no mesmo flush — evita falso positivo.
    """
    cliente = Customer(name="Maria")
    session.add(cliente)
    session.commit()

    cliente.name = "Maria Silva"
    session.commit()  # não deve lançar, Customer não tem campo stock
    assert cliente.name == "Maria Silva"