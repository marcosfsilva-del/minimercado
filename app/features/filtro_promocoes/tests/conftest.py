from types import SimpleNamespace

import pytest
from sqlalchemy import create_engine, delete, select
from sqlalchemy.orm import sessionmaker

from app.core import create_app
from app.core import database as database_module
from app.core.models import Product

NOMES_PROMOCIONAIS = ("Arroz Promo", "Cafe Promo")
NOMES_COMUNS = ("Feijao Comum", "Leite Comum")


def criar_produto(nome: str, promocional: bool) -> Product:
    return Product(
        name=nome,
        description=f"Descricao de {nome}",
        category="Mercearia",
        price=10.0,
        stock=5,
        promotional=promocional,
    )


@pytest.fixture()
def dados():
    return SimpleNamespace(promocionais=NOMES_PROMOCIONAIS, comuns=NOMES_COMUNS)


@pytest.fixture()
def session_factory(tmp_path, monkeypatch):
    """Banco SQLite isolado por teste, injetado no escopo de sessao do core."""
    database_path = (tmp_path / "filtro_promocoes.db").as_posix()
    engine = create_engine(f"sqlite:///{database_path}", future=True)
    factory = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
    monkeypatch.setattr(database_module, "engine", engine)
    monkeypatch.setattr(database_module, "SessionLocal", factory)

    yield factory

    engine.dispose()


@pytest.fixture()
def app(session_factory, dados):
    application = create_app()

    with session_factory() as session:
        session.add_all([criar_produto(nome, True) for nome in dados.promocionais])
        session.add_all([criar_produto(nome, False) for nome in dados.comuns])
        session.commit()

    return application


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def session(app, session_factory):
    with session_factory() as open_session:
        yield open_session


@pytest.fixture()
def sem_promocoes(app, session_factory):
    """Deixa o catalogo apenas com produtos nao promocionais."""
    with session_factory() as open_session:
        open_session.execute(delete(Product).where(Product.promotional.is_(True)))
        open_session.commit()


@pytest.fixture()
def criar_promocao(session_factory):
    """Insere uma promocao no catalogo depois do app ja estar montado."""

    def _criar_promocao(nome: str) -> None:
        with session_factory() as open_session:
            open_session.add(criar_produto(nome, True))
            open_session.commit()

    return _criar_promocao


@pytest.fixture()
def desativar_promocao(session_factory):
    """Desliga a promocao de um produto existente, sem remove-lo do catalogo."""

    def _desativar(nome: str) -> None:
        with session_factory() as open_session:
            produto = open_session.scalar(select(Product).where(Product.name == nome))
            produto.promotional = False
            open_session.commit()

    return _desativar
