from app.core.types.features import FeatureManifest, SlotContribution
from app.features.limpar_carrinho.routes import bp, render_botao_limpar

manifest = FeatureManifest(
    id="025",
    name="Botao Limpar Carrinho",
    blueprint=bp,
    menu=None,
    slots=[SlotContribution(slot="CART_SUMMARY", renderer=render_botao_limpar)],
)
