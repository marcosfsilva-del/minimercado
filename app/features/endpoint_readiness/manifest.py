from app.core.types.features import FeatureManifest, MenuItem
from app.features.endpoint_readiness.routes import bp

manifest = FeatureManifest(
    id="endpoint-readiness",
    name="Endpoint Readiness",
    blueprint=bp,
    menu=MenuItem(label="Endpoint Readiness", endpoint="endpoint_readiness.page", order=50),
    slots=[],
)
