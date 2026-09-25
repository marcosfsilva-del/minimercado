from flask import Blueprint, jsonify, request

from app.core.config import settings
from app.core.database import session_scope
from app.core.services.market_service import (
    create_order,
    list_inventory_movements,
    list_orders,
    list_products,
    movement_to_dict,
    order_to_dict,
    product_to_dict,
)

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.get("")
def index():
    return jsonify({"name": "DevOps Market", "status": "online"})


@api_bp.get("/health")
def health():
    return jsonify(
        {"status": "ok", "version": settings.app_version, "commit": settings.commit_sha}
    )


@api_bp.get("/ready")
def ready():
    return jsonify({"status": "ready"})


@api_bp.get("/products")
def products():
    with session_scope() as db:
        return jsonify([product_to_dict(product) for product in list_products(db)])


@api_bp.get("/orders")
def orders():
    with session_scope() as db:
        return jsonify([order_to_dict(order) for order in list_orders(db)])


@api_bp.post("/orders")
def create_order_api():
    data = request.get_json(silent=True) or {}
    items = [
        {"product_id": int(item["productId"]), "quantity": int(item["quantity"])}
        for item in data.get("items", [])
    ]
    with session_scope() as db:
        order = create_order(db, items, data.get("customerName"))
        return jsonify(order_to_dict(order)), 201


@api_bp.get("/inventory/movements")
def inventory_movements():
    """Lista todas as movimentações de estoque ordenadas da mais recente para a mais antiga."""
    with session_scope() as db:
        return jsonify(
            [movement_to_dict(m) for m in list_inventory_movements(db)]
        )
