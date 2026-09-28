from app.core.types.features import FeatureManifest, MenuItem
from app.features.free_shipping.routes import bp

manifest = FeatureManifest(
    id="free-shipping",
    name="Free Shipping",
    blueprint=bp,
    menu=MenuItem(label="Free Shipping", endpoint="free_shipping.page", order=50),
    slots=[],
)