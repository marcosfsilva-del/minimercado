from flask import render_template

from app.core.types.features import FeatureManifest, MenuItem, SlotContribution
from app.features.coupon.routes import bp


def cart_summary_field(**context) -> str:
    return render_template("coupon_field.html", total=context.get("total"))


manifest = FeatureManifest(
    id="coupon",
    name="Cupom",
    blueprint=bp,
    menu=MenuItem(label="Cupom", endpoint="coupon.page", order=50),
    slots=[SlotContribution(slot="CART_SUMMARY", renderer=cart_summary_field)],
)