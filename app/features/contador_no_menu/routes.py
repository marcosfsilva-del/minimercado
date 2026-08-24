from flask import Blueprint, jsonify, render_template

from app.features.contador_no_menu.service import status

bp = Blueprint("contador_no_menu", __name__, url_prefix="/contador-no-menu", template_folder="templates")


@bp.get("")
def page():
    return render_template("contador-no-menu.html")


@bp.get("/api")
def api():
    return jsonify(status())
