
from app.features.vistos_recentemente.service import registrar_visualizacao


def test_registro_produto_visualizado():
    historico = []

    resultado = registrar_visualizacao(historico, produto_id=1)

    assert resultado == [1]


def test_ordem_produtos_recentes():
    historico = []

    historico = registrar_visualizacao(historico, produto_id=1)
    historico = registrar_visualizacao(historico, produto_id=2)

    assert historico == [2, 1]


def test_remocao_duplicados():
    historico = []

    historico = registrar_visualizacao(historico, produto_id=1)
    historico = registrar_visualizacao(historico, produto_id=2)
    historico = registrar_visualizacao(historico, produto_id=1)

    assert historico == [1, 2]
