from app.features.listar_movimentacoes.service import status


def test_status():
    assert status() == {"feature": "listar-movimentacoes", "status": "ok"}
