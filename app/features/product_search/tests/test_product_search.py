from app.features.product_search.service import status


def test_status():
    assert status() == {"feature": "product-search", "status": "ok"}
