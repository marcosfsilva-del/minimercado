from flask import Blueprint, jsonify, render_template

from app.features.bloquear_estoque_negativo.service import (
    InsufficientStockError,
    status,
)

bp = Blueprint(
    "bloquear_estoque_negativo",
    __name__,
    url_prefix="/bloquear-estoque-negativo",
    template_folder="templates",
)


@bp.record_once
def _register_error_handlers(state):
    """
    Garante respostas HTTP decentes (em vez de 500 genérico) para:
    - InsufficientStockError: gerada pelo nosso listener (caso de
      itens duplicados no carrinho, que o core não cobre sozinho)
    - ValueError: cobre as validações que já existiam em
      market_service.create_order (quantidade, produto, estoque),
      que nunca tinham tratamento HTTP antes desta feature.
    Efeito é global no app (não só nas rotas desta feature), mas
    substitui um 500 sem informação por uma resposta com mensagem —
    estritamente uma melhoria, sem mudar nenhum arquivo do core.
    """
    state.app.register_error_handler(
        InsufficientStockError,
        lambda e: (jsonify({"error": str(e)}), 409),
    )
    state.app.register_error_handler(
        ValueError,
        lambda e: (jsonify({"error": str(e)}), 409),
    )


@bp.get("")
def page():
    return render_template("bloquear-estoque-negativo.html")


@bp.get("/api")
def api():
    return jsonify(status())