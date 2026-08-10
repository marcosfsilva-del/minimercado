from app.core import create_app


def test_catalog_page_renders():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Catalogo" in response.data
