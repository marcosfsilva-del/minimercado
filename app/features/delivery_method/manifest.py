from app.core.types.features import FeatureManifest, MenuItem
from app.features.delivery_method.routes import bp

manifest = FeatureManifest(
    id="delivery-method",
    name="Delivery Method",
    blueprint=bp,
    menu=MenuItem(label="Delivery Method", endpoint="delivery_method.page", order=50),
    slots=[],
)
