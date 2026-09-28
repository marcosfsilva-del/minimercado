from app.core.types.features import FeatureManifest
from app.features.bloquear_estoque_negativo.routes import bp

manifest = FeatureManifest(
    id="bloquear-estoque-negativo",
    name="Bloquear Estoque Negativo",
    blueprint=bp,
    slots=[],
)