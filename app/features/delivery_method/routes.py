from flask import Blueprint, jsonify, render_template

from app.features.delivery_method.service import status

bp = Blueprint(
    "delivery_method",
    __name__,
    url_prefix="/delivery-method",
    template_folder="templates",
)


@bp.get("")
def page():
    return render_template("delivery-method.html")


@bp.get("/api")
def api():
    return jsonify(status())