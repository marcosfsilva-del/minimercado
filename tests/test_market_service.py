import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.core.database import Base
from app.core.models import Product
from app.core.services.market_service import create_order, list_products


def test_create_order_rejects_empty_items():
    with pytest.raises(ValueError, match="pelo menos um item"):
        create_order(session=None, items=[])  # type: ignore[arg-type]


@pytest.fixture
def db():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        yield session


@pytest.fixture
def products(db):
    products = [
        Product(
            name="Banana",
            description="Banana prata",
            category="Frutas",
            price=5.0,
            stock=10,
        ),
        Product(
            name="Arroz",
            description="Arroz branco",
            category="Alimentos",
            price=20.0,
            stock=10,
        ),
        Product(
            name="Cafe",
            description="Cafe em po",
            category="Bebidas",
            price=10.0,
            stock=10,
        ),
    ]

    db.add_all(products)
    db.commit()

    return products


def test_list_products_orders_name_ascending(db, products):
    result = list_products(db, sort_by="name")

    assert [product.name for product in result] == [
        "Arroz",
        "Banana",
        "Cafe",
    ]


def test_list_products_orders_name_descending(db, products):
    result = list_products(db, sort_by="name", descending=True)

    assert [product.name for product in result] == [
        "Cafe",
        "Banana",
        "Arroz",
    ]


def test_list_products_orders_price_ascending(db, products):
    result = list_products(db, sort_by="price")

    assert [product.price for product in result] == [
        5.0,
        10.0,
        20.0,
    ]


def test_list_products_orders_price_descending(db, products):
    result = list_products(db, sort_by="price", descending=True)

    assert [product.price for product in result] == [
        20.0,
        10.0,
        5.0,
    ]
