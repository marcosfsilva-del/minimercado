from app.core.types.features import FeatureManifest, MenuItem
from app.features.bloquear_estoque_negativo.routes import bp

manifest = FeatureManifest(
    id="bloquear-estoque-negativo",
    name="Bloquear Estoque Negativo",
    blueprint=bp,
    menu=MenuItem(
    label="Bloquear Estoque Negativo",
    endpoint="bloquear_estoque_negativo.page",
    order=50,),
    slots=[],
)
