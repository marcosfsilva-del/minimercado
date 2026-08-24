from app.core.types.features import FeatureManifest, MenuItem
from app.features.contador_no_menu.routes import bp

manifest = FeatureManifest(
    id="contador-no-menu",
    name="Contador No Menu",
    blueprint=bp,
    menu=MenuItem(label="Contador No Menu", endpoint="contador_no_menu.page", order=50),
    slots=[],
)
