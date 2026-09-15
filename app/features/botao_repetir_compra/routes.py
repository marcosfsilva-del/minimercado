from flask import Blueprint, jsonify, render_template

from app.features.botao_repetir_compra.service import status

bp = Blueprint("botao_repetir_compra", __name__, url_prefix="/botao-repetir-compra", template_folder="templates")


@bp.get("")
def page():
    return render_template("botao-repetir-compra.html")


@bp.get("/api")
def api():
    return jsonify(status())
