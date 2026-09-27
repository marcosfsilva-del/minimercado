from flask import Blueprint, jsonify, render_template

from app.core.database import session_scope
from app.features.filtro_promocoes.service import (
    list_promotional_products,
    promotional_product_to_dict,
)

bp = Blueprint(
    "filtro_promocoes",
    __name__,
    url_prefix="/promocoes",
    template_folder="templates",
)


@bp.get("")
def page():
    with session_scope() as db:
        products = list_promotional_products(db)
    return render_template("filtro-promocoes.html", products=products)


@bp.get("/api")
def api():
    with session_scope() as db:
        products = list_promotional_products(db)
    return jsonify([promotional_product_to_dict(product) for product in products])
