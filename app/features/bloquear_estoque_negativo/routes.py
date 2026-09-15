from flask import Blueprint, jsonify, render_template

from app.features.bloquear_estoque_negativo.service import status

bp = Blueprint(
    "bloquear_estoque_negativo",
    __name__,
    url_prefix="/bloquear-estoque-negativo",
    template_folder="templates",
)


@bp.get("")
def page():
    return render_template("bloquear-estoque-negativo.html")


@bp.get("/api")
def api():
    return jsonify(status())
