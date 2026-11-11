
from flask import Blueprint, redirect, session, url_for

from app.features.vistos_recentemente.service import registrar_visualizacao

vistos_bp = Blueprint(
    "vistos_recentemente",
    __name__,
    url_prefix="/vistos-recentemente",
)


@vistos_bp.post("/registrar/<int:produto_id>")
def registrar_produto(produto_id: int):
    historico = session.get("vistos_recentemente", [])

    session["vistos_recentemente"] = registrar_visualizacao(
        historico, produto_id
    )

    return redirect(url_for("web.catalog"))
