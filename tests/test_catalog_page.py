from app.core import create_app


def test_catalog_page_renders():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert "Catálogo".encode() in response.data


def test_catalog_filter_by_min_price():
    app = create_app()
    client = app.test_client()

    response = client.get("/?min_price=100")

    assert response.status_code == 200
    assert "Catálogo".encode() in response.data


def test_catalog_filter_by_max_price():
    app = create_app()
    client = app.test_client()

    response = client.get("/?max_price=50")

    assert response.status_code == 200
    assert "Catálogo".encode() in response.data


def test_catalog_filter_by_price_range():
    app = create_app()
    client = app.test_client()

    response = client.get("/?min_price=50&max_price=150")

    assert response.status_code == 200
    assert "Catálogo".encode() in response.data
