from sqlalchemy import event
from sqlalchemy.orm import Session

from app.core.models import Product


class InsufficientStockError(ValueError):
    """Levantado quando uma operação deixaria o estoque negativo."""


@event.listens_for(Session, "before_flush")
def _bloquear_estoque_negativo(session, flush_context, instances):
    """
    Intercepta qualquer fluxo que tente persistir um Product com
    estoque negativo, bloqueando antes de chegar ao banco.
    Não depende de nenhuma alteração em app/core/*.
    """
    for obj in session.dirty:
        if isinstance(obj, Product) and obj.stock is not None and obj.stock < 0:
            raise InsufficientStockError(
                f"Estoque insuficiente para {obj.name}. "
                f"A operação deixaria o estoque em {obj.stock}, "
                f"o que não é permitido."
            )


def status() -> dict[str, str]:
    return {"feature": "bloquear-estoque-negativo", "status": "ok"}