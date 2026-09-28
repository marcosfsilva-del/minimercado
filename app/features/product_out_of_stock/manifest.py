from app.core.models import Product
from app.core.types.features import FeatureManifest, SlotContribution
from app.features.product_out_of_stock.service import out_of_stock_label


def product_card_badge(*, product: Product) -> str:
    label = out_of_stock_label(product.stock)
    if label is None:
        return ""
    return f'<span class="badge" role="status">{label}</span>'

manifest = FeatureManifest(
    id="product-out-of-stock",
    name="Sinalização De Produto Esgotado",
    slots=[SlotContribution(slot="PRODUCT_CARD", renderer=product_card_badge)],
)
