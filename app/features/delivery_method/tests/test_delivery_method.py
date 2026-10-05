from app.features.delivery_method.service import status


def test_status():
    assert status() == {"feature": "delivery-method", "status": "ok"}
