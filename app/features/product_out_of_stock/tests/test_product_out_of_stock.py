from app.core import create_app
from app.core.models import Product
from app.features.product_out_of_stock.service import out_of_stock_label


def test_zero_stock_is_out_of_stock():
    assert out_of_stock_label(0) == "Esgotado"


def test_positive_stock_is_not_out_of_stock():
    assert out_of_stock_label(1) is None


def test_catalog_shows_sold_out_product_and_disables_add_button(monkeypatch):
    product = Product(
        id=999,
        name="Produto esgotado de teste",
        description="Produto para validar estoque zero",
        category="Teste",
        price=10.0,
        stock=0,
        promotional=False,
    )
    monkeypatch.setattr("app.core.routes.web.list_products", lambda _db: [product])
    client = create_app().test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Produto esgotado de teste" in response.data
    assert b'<span class="badge" role="status">Esgotado</span>' in response.data
    assert b'<button type="submit" disabled>' in response.data
