from app.core.types.features import FeatureManifest
from app.features.success.routes import success_bp


manifest = FeatureManifest(
    id="success",
    name="Tela de Sucesso",
    blueprint=success_bp,
)
