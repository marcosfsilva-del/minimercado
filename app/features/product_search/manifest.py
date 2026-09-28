from flask import render_template

from app.core.types.features import FeatureManifest, SlotContribution
from app.features.product_search.routes import bp


def render_search_toolbar(**_context) -> str:
    return render_template("product_search_toolbar.html")


manifest = FeatureManifest(
    id="product-search",
    name="Product Search",
    blueprint=bp,
    menu=None,
    slots=[
        SlotContribution(
            slot="PRODUCT_LIST_TOOLBAR",
            renderer=render_search_toolbar,
        )
    ],
)
