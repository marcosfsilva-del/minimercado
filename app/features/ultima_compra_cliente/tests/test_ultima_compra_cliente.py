from app.features.ultima_compra_cliente.service import status


def test_status():
    assert status() == {"feature": "ultima-compra-cliente", "status": "ok"}
