"""Rotas HTTP da feature de readiness."""

from flask import Blueprint, jsonify, render_template

from .service import check_readiness

bp = Blueprint(
    "endpoint_readiness",
    __name__,
    template_folder="templates",
)


@bp.route("/", methods=["GET"])
def page():
    """Página da feature exibida no menu."""
    return render_template("endpoint-readiness.html")


@bp.route("/readiness", methods=["GET"])
def readiness():
    """
    GET /readiness - Issue #19 (Requisito 103).

    Retorna JSON indicando se a aplicação pode receber tráfego.
    """
    resultado = check_readiness()
    status_code = 200 if resultado["status"] == "ready" else 503
    return jsonify(resultado), status_code