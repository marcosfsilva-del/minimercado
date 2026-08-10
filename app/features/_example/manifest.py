from app.core.types.features import FeatureManifest, MenuItem, SlotContribution
from app.features._example.routes import example_bp


def toolbar_badge(**_context) -> str:
    return '<span class="badge">Slot de exemplo</span>'


manifest = FeatureManifest(
    id="example",
    name="Feature de Exemplo",
    blueprint=example_bp,
    menu=MenuItem(label="Exemplo", endpoint="example.page", order=99),
    slots=[SlotContribution(slot="PRODUCT_LIST_TOOLBAR", renderer=toolbar_badge)],
)
