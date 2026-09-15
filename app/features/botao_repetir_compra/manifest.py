from app.core.types.features import FeatureManifest, MenuItem
from app.features.botao_repetir_compra.routes import bp

manifest = FeatureManifest(
    id="botao-repetir-compra",
    name="Botao Repetir Compra",
    blueprint=bp,
    menu=MenuItem(label="Botao Repetir Compra", endpoint="botao_repetir_compra.page", order=50),
    slots=[],
)
