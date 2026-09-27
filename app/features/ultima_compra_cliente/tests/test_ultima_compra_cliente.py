from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.core.database import Base
from app.core.models import Customer, Order
from app.features.ultima_compra_cliente.service import get_last_purchase, status


def create_test_session() -> Session:
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    return Session(engine)


def test_status():
    assert status() == {"feature": "ultima-compra-cliente", "status": "ok"}


def test_get_last_purchase_returns_none_when_customer_has_no_orders():
    with create_test_session() as session:
        customer = Customer(name="João")
        session.add(customer)
        session.flush()

        result = get_last_purchase(session, customer)

        assert result is None


def test_get_last_purchase_returns_customer_order():
    with create_test_session() as session:
        customer = Customer(name="João")
        order = Order(
            customer_name="João",
            total=100.0,
            created_at=datetime(2026, 9, 10, 10, 0),
        )

        session.add_all([customer, order])
        session.flush()

        result = get_last_purchase(session, customer)

        assert result is not None
        assert result.id == order.id
        assert result.created_at == order.created_at


def test_get_last_purchase_returns_most_recent_order():
    with create_test_session() as session:
        customer = Customer(name="João")

        older_order = Order(
            customer_name="João",
            total=50.0,
            created_at=datetime(2026, 9, 1, 10, 0),
        )

        newer_order = Order(
            customer_name="João",
            total=150.0,
            created_at=datetime(2026, 9, 20, 10, 0),
        )

        other_customer_order = Order(
            customer_name="Ana",
            total=300.0,
            created_at=datetime(2026, 9, 25, 10, 0),
        )

        session.add_all(
            [
                customer,
                older_order,
                newer_order,
                other_customer_order,
            ]
        )
        session.flush()

        result = get_last_purchase(session, customer)

        assert result is not None
        assert result.id == newer_order.id
        assert result.created_at == newer_order.created_at