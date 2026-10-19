from sqlalchemy import delete

from app.core import create_app
from app.core.database import session_scope
from app.core.models import Product


def test_catalog_page_renders():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert "Catálogo".encode() in response.data


def _prepare_filter_products() -> None:
    with session_scope() as db:
        db.execute(delete(Product).where(Product.name.like("TesteFiltro%")))
        db.add_all(
            [
                Product(
                    name="TesteFiltro Barato",
                    description="Produto de teste barato",
                    category="Teste",
                    price=5.0,
                    stock=10,
                    promotional=False,
                ),
                Product(
                    name="TesteFiltro Médio",
                    description="Produto de teste médio",
                    category="Teste",
                    price=12.0,
                    stock=10,
                    promotional=False,
                ),
                Product(
                    name="TesteFiltro Caro",
                    description="Produto de teste caro",
                    category="Teste",
                    price=25.0,
                    stock=10,
                    promotional=False,
                ),
            ]
        )


def test_catalog_page_price_filter_and_clear():
    app = create_app()
    client = app.test_client()
    _prepare_filter_products()

    filtered = client.get("/?min_price=10&max_price=20")
    assert filtered.status_code == 200
    assert b"TesteFiltro M\xc3\xa9dio" in filtered.data
    assert b"TesteFiltro Barato" not in filtered.data
    assert b"TesteFiltro Caro" not in filtered.data
    assert b"Limpar filtro" in filtered.data

    cleared = client.get("/")
    assert cleared.status_code == 200
    assert b"TesteFiltro Barato" in cleared.data
    assert b"TesteFiltro M\xc3\xa9dio" in cleared.data
    assert b"TesteFiltro Caro" in cleared.data
