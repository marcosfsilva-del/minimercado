import pytest
from flask import Flask, session

from app.features.limpar_carrinho.service import CarrinhoCleanerService, executar_limpeza


@pytest.fixture
def app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "test-secret-key"
    return app


def test_limpar_remove_todos_os_itens_do_carrinho(app: Flask):
    with app.test_request_context():
        session["cart"] = {"1": 2, "3": 5}

        resultado = CarrinhoCleanerService().limpar()

        assert resultado is True
        assert session["cart"] == {}


def test_limpar_com_carrinho_ja_vazio_retorna_true_e_mantem_vazio(app: Flask):
    with app.test_request_context():
        session["cart"] = {}

        resultado = executar_limpeza()

        assert resultado is True
        assert session["cart"] == {}


def test_limpar_sem_carrinho_iniciado_na_sessao_retorna_false(app: Flask):
    with app.test_request_context():
        resultado = executar_limpeza()

        assert resultado is False
        assert "cart" not in session
