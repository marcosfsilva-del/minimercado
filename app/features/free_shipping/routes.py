from flask import Blueprint, jsonify, render_template, request

from app.features.free_shipping.service import status, summary

bp = Blueprint(
    "free_shipping",
    __name__,
    url_prefix="/free-shipping",
    template_folder="templates",
)


@bp.get("")
def page():
    return render_template("free-shipping.html")


@bp.get("/api")
def api():
    subtotal = request.args.get("subtotal", default=0.0, type=float)
    return jsonify({**status(), **summary(subtotal)})