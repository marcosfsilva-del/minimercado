from types import SimpleNamespace

from app.core import create_app
from app.features.product_search.service import search_products, status


def test_status():
    assert status() == {"feature": "product-search", "status": "ok"}


def test_search_products_by_name():
    products = [
        SimpleNamespace(name="Arroz Branco", description="Pacote 5kg"),
        SimpleNamespace(name="Feijão Preto", description="Pacote 1kg"),
        SimpleNamespace(name="Macarrão Espaguete", description="Pacote 500g"),
    ]

    results = search_products(products, "arroz")
    assert len(results) == 1
    assert results[0].name == "Arroz Branco"

    results_upper = search_products(products, "FEIJÃO")
    assert len(results_upper) == 1
    assert results_upper[0].name == "Feijão Preto"


def test_search_products_hides_unmatched():
    products = [
        SimpleNamespace(name="Arroz Branco", description="Pacote 5kg"),
        SimpleNamespace(name="Feijão Preto", description="Pacote 1kg"),
    ]

    results = search_products(products, "chocolate")
    assert len(results) == 0


def test_search_products_empty_returns_all():
    products = [
        SimpleNamespace(name="Arroz Branco", description="Pacote 5kg"),
        SimpleNamespace(name="Feijão Preto", description="Pacote 1kg"),
    ]

    assert search_products(products, "") == products
    assert search_products(products, "   ") == products
    assert search_products(products, None) == products


def test_catalog_renders_search_toolbar():
    app = create_app()
    client = app.test_client()

    response = client.get("/")
    assert response.status_code == 200
    html = response.data.decode("utf-8")
    assert 'id="product-search-input"' in html
    assert "Buscar produto por nome..." in html
    assert "product-grid" in html
