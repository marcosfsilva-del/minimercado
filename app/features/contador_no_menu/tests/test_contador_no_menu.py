from app.features.contador_no_menu.service import total_items


def test_soma_quantidades_de_varios_produtos():
    cart = {"1": 2, "2": 3}
    assert total_items(cart) == 5


def test_conta_quantidade_nao_produtos_distintos():
    # 1 produto só, mas quantidade 5 -> deve contar 5, não 1
    cart = {"1": 5}
    assert total_items(cart) == 5


def test_carrinho_vazio_retorna_zero():
    assert total_items({}) == 0