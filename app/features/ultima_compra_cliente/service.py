from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.models import Customer, Order


def status() -> dict[str, str]:
    return {"feature": "ultima-compra-cliente", "status": "ok"}

def get_last_purchase(session: Session, customer: Customer) -> Order | None:
    statement = (
        select(Order)
        .where(Order.customer_name == customer.name)
        .order_by(Order.created_at.desc())
        .limit(1)
    )

    return session.scalar(statement)