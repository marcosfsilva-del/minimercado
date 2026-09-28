from app.features.coupon.service import status


def test_status():
    assert status() == {"feature": "coupon", "status": "ok"}
