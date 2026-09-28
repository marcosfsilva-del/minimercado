from flask import Blueprint, abort, flash, redirect, session, url_for

from app.core.database import session_scope
from app.features.repeat_order.service import repeat_order

bp = Blueprint("repeat_order", __name__, url_prefix="/repeat-order")


@bp.post("/<int:order_id>")
def repeat(order_id: int):
    cart = session.setdefault("cart", {})
    with session_scope() as db:
        try:
            result = repeat_order(db, order_id, cart)
        except ValueError:
            abort(404)
    session.modified = True

    if result["adjusted"] or result["unavailable"]:
        flash("Alguns itens foram ajustados ao estoque disponível.")
    else:
        flash("Itens do pedido adicionados ao carrinho.")
    return redirect(url_for("web.cart"))
