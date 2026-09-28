from flask import Blueprint, redirect, url_for

from app.features.limpar_carrinho.service import executar_limpeza

bp = Blueprint("feature_025", __name__, url_prefix="/limpar-carrinho", template_folder="templates")


@bp.post("/executar")
def limpar_carrinho_action():
    """Rota POST disparada quando o usuario clica no botao 'Limpar Carrinho'."""
    executar_limpeza()

    # Redireciona o usuario de volta para a pagina do carrinho (padrao POST-Redirect-GET)
    return redirect(url_for("web.cart"))


def render_botao_limpar(**_contexto) -> str:
    """Renderiza o botao 'Limpar Carrinho' exibido no resumo do carrinho.

    Esta funcao e registrada como SlotContribution do slot CART_SUMMARY
    (ver manifest.py) e por isso e chamada pelo core com os kwargs
    `items` e `total` (veja app/core/templates/cart.html). Eles nao sao
    usados aqui, mas precisam ser aceitos para nao quebrar a chamada.
    """
    action_url = url_for("feature_025.limpar_carrinho_action")
    return (
        '<form method="post" action="' + action_url + '">'
        '<button type="submit" class="secondary full">Limpar Carrinho</button>'
        "</form>"
    )
