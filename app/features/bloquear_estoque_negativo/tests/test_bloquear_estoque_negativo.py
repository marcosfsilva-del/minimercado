from app.features.bloquear_estoque_negativo.service import status


def test_status():
    assert status() == {"feature": "bloquear-estoque-negativo", "status": "ok"}
