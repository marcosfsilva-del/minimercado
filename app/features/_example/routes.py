from flask import Blueprint, jsonify, render_template

example_bp = Blueprint(
    "example",
    __name__,
    url_prefix="/example",
    template_folder="templates",
)


@example_bp.get("")
def page():
    return render_template("example.html")


@example_bp.get("/api")
def api():
    return jsonify({"message": "example"})
