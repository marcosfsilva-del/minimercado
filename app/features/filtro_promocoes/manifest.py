from flask import url_for

from app.core.types.features import FeatureManifest, MenuItem, SlotContribution
from app.features.filtro_promocoes.routes import bp

LABEL = "Ver promoções"


def promotions_link(**_context) -> str:
    return (
        f'<a class="button-link" id="ver-promocoes" href="{url_for("filtro_promocoes.page")}">'
        f"{LABEL}</a>"
    )


manifest = FeatureManifest(
    id="filtro-promocoes",
    name="Filtro de Promoções",
    blueprint=bp,
    menu=MenuItem(label=LABEL, endpoint="filtro_promocoes.page", order=20),
    slots=[SlotContribution(slot="PRODUCT_LIST_TOOLBAR", renderer=promotions_link)],
)
