
from flask import session, url_for
from markupsafe import escape

from app.core.types.features import FeatureManifest, SlotContribution
from app.features.vistos_recentemente.routes import vistos_bp


def botao_visualizar(product):
    url = url_for(
        "vistos_recentemente.registrar_produto",
        produto_id=product.id,
    )

    return (
        f'<form method="post" action="{escape(url)}">'
        '<button type="submit">Visualizar produto</button>'
        '</form>'
    )


def mostrar_recentes(products):
    historico = session.get("vistos_recentemente", [])

    if not historico:
        return ""

    produtos_por_id = {produto.id: produto for produto in products}

    nomes = [
        str(escape(produtos_por_id[produto_id].name))
        for produto_id in historico
        if produto_id in produtos_por_id
    ]

    if not nomes:
        return ""

    return (
        '<div class="recentes">'
        '<strong>Vistos recentemente:</strong> '
        + ", ".join(nomes)
        + "</div>"
    )


manifest = FeatureManifest(
    id="vistos_recentemente",
    name="Vistos Recentemente",
    blueprint=vistos_bp,
    slots=[
        SlotContribution(
            slot="PRODUCT_CARD",
            renderer=botao_visualizar,
        ),
        SlotContribution(
            slot="PRODUCT_LIST_TOOLBAR",
            renderer=mostrar_recentes,
        ),
    ],
)
