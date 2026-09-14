from flask import Blueprint, jsonify, render_template

from app.features.endpoint_readiness.service import status

bp = Blueprint("endpoint_readiness", __name__, url_prefix="/endpoint-readiness", template_folder="templates")


@bp.get("")
def page():
    return render_template("endpoint-readiness.html")


@bp.get("/api")
def api():
    return jsonify(status())
