from flask import url_for

from app.core.types.features import FeatureManifest, SlotContribution
from app.features.repeat_order.routes import bp


def repeat_button(order, **_context) -> str:
    action = url_for("repeat_order.repeat", order_id=order.id)
    return f'<form method="post" action="{action}"><button type="submit">Repetir</button></form>'


manifest = FeatureManifest(
    id="repeat-order",
    name="Repetir Compra",
    blueprint=bp,
    slots=[SlotContribution(slot="ORDER_SUMMARY", renderer=repeat_button)],
)
