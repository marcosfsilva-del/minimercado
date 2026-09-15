from app.features.botao_repetir_compra.service import status


def test_status():
    assert status() == {"feature": "botao-repetir-compra", "status": "ok"}
