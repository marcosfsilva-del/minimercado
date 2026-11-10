from app.core.database import session_scope
from app.core.models import Order


def get_order(order_id: int) -> Order | None:
    with session_scope() as db:
        return db.get(Order, order_id)
