from flask import Blueprint, jsonify, render_template

from app.features.ultima_compra_cliente.service import status

bp = Blueprint(
    "ultima_compra_cliente",
    __name__,
    url_prefix="/ultima-compra-cliente",
    template_folder="templates",
)

@bp.get("")
def page():
    return render_template("ultima-compra-cliente.html")


@bp.get("/api")
def api():
    return jsonify(status())
