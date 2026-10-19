import pytest
from sqlalchemy import delete

from app.core.database import init_database, session_scope
from app.core.models import Product
from app.core.services.market_service import create_order, list_products


def test_create_order_rejects_empty_items():
    with pytest.raises(ValueError, match="pelo menos um item"):
        create_order(session=None, items=[])  # type: ignore[arg-type]


def _prepare_filter_products() -> None:
    init_database()
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


def _filter_test_names(products: list[Product]) -> list[str]:
    return sorted(product.name for product in products if product.name.startswith("TesteFiltro"))


def test_list_products_filters_by_min_price():
    _prepare_filter_products()
    with session_scope() as db:
        products = list_products(db, min_price=12.0)

    assert _filter_test_names(products) == ["TesteFiltro Caro", "TesteFiltro Médio"]


def test_list_products_filters_by_max_price():
    _prepare_filter_products()
    with session_scope() as db:
        products = list_products(db, max_price=12.0)

    assert _filter_test_names(products) == ["TesteFiltro Barato", "TesteFiltro Médio"]


def test_list_products_filters_by_min_and_max_price():
    _prepare_filter_products()
    with session_scope() as db:
        products = list_products(db, min_price=10.0, max_price=20.0)

    assert _filter_test_names(products) == ["TesteFiltro Médio"]
