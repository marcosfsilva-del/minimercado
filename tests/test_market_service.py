import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.core.database import Base
from app.core.models import Product
from app.core.services.market_service import create_order


def test_create_order_rejects_empty_items():
    with pytest.raises(ValueError, match="pelo menos um item"):
        create_order(session=None, items=[])  # type: ignore[arg-type]


def test_create_order_saves_cpf():
    engine = create_engine("sqlite:///:memory:")

    Base.metadata.create_all(engine)

    with Session(engine) as db:
        product = Product(
            name="Produto teste",
            description="Produto usado no teste",
            category="Teste",
            price=10.00,
            stock=10,
            promotional=False,
        )

        db.add(product)
        db.flush()

        order = create_order(
            db,
            [{"product_id": product.id, "quantity": 1}],
            "Rafa",
            "123.456.789-00",
        )

        assert order.cpf == "123.456.789-00"


def test_create_order_accepts_cpf_without_punctuation():
    engine = create_engine("sqlite:///:memory:")

    Base.metadata.create_all(engine)

    with Session(engine) as db:
        product = Product(
            name="Produto teste",
            description="Produto usado no teste",
            category="Teste",
            price=10.00,
            stock=10,
            promotional=False,
        )

        db.add(product)
        db.flush()

        order = create_order(
            db,
            [{"product_id": product.id, "quantity": 1}],
            "Rafa",
            "12345678900",
        )

        assert order.cpf == "12345678900"