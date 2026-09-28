from flask import Blueprint, jsonify, render_template, request

from app.core.database import session_scope
from app.core.services.market_service import list_products
from app.features.product_search.service import search_products, status

bp = Blueprint(
    "product_search",
    __name__,
    url_prefix="/product-search",
    template_folder="templates",
)


@bp.get("")
def page():
    query = request.args.get("q", "")
    with session_scope() as db:
        products = list_products(db)
    filtered = search_products(products, query)
    return render_template("product-search.html", products=filtered, query=query)


@bp.get("/api")
def api():
    query = request.args.get("q")
    if query is not None:
        with session_scope() as db:
            products = list_products(db)
        filtered = search_products(products, query)
        return jsonify(
            [
                {
                    "id": p.id,
                    "name": p.name,
                    "price": p.price,
                    "category": p.category,
                    "description": p.description,
                }
                for p in filtered
            ]
        )
    return jsonify(status())
