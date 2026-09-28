from flask import session

from app.core.types.features import FeatureManifest, SlotContribution
from app.features.contador_no_menu.service import total_items


def render_counter() -> str:
    total = total_items(session.get("cart", {}))
    if total == 0:
        return ""
    return f'<span class="cart-counter">{total}</span>'


manifest = FeatureManifest(
    id="contador-no-menu",
    name="Contador No Menu",
    slots=[SlotContribution(slot="MAIN_MENU", renderer=render_counter)],
)