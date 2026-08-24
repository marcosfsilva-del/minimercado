from app.core.types.features import FeatureManifest, MenuItem
from app.features.product_search.routes import bp

manifest = FeatureManifest(
    id="product-search",
    name="Product Search",
    blueprint=bp,
    menu=MenuItem(label="Product Search", endpoint="product_search.page", order=50),
    slots=[],
)
