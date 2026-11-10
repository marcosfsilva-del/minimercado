from flask import Blueprint, abort, render_template

from app.features.success.service import get_order

success_bp = Blueprint(
    "success",
    __name__,
    url_prefix="/success",
    template_folder="templates",
)


@success_bp.get("/<int:order_id>")
def index(order_id: int):
    order = get_order(order_id)

    if order is None:
        abort(404)

    return render_template("success.html", order=order)
