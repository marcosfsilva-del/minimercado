from app.core.types.features import FeatureManifest, MenuItem
from app.features.ultima_compra_cliente.routes import bp

manifest = FeatureManifest(
    id="ultima-compra-cliente",
    name="Ultima Compra Cliente",
    blueprint=bp,
    menu=MenuItem(label="Ultima Compra Cliente", endpoint="ultima_compra_cliente.page", order=50),
    slots=[],
)
