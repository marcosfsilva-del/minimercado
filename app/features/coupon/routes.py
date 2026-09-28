from flask import Blueprint, jsonify, render_template, request

from app.features.coupon.service import COUPONS, apply_coupon, status

bp = Blueprint("coupon", __name__, url_prefix="/coupon", template_folder="templates")


@bp.get("")
def page():
    return render_template("coupon.html", coupons=COUPONS)


@bp.post("/apply")
def apply():
    code = request.form.get("code", "")
    total = float(request.form.get("total") or 0)
    result = apply_coupon(code, total)
    return render_template("coupon.html", result=result, coupons=COUPONS)


@bp.get("/api")
def api():
    return jsonify(status())