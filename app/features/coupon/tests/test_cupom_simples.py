from app.features.coupon.service import apply_coupon


def test_cupom_valido_e_reconhecido():
    resultado = apply_coupon("DEVOPS10", 100.0)

    assert resultado["valid"] is True
    assert resultado["code"] == "DEVOPS10"


def test_cupom_invalido_nao_e_reconhecido():
    resultado = apply_coupon("INVALIDO", 100.0)

    assert resultado["valid"] is False
    assert resultado["discount"] == 0.0
    assert resultado["total"] == 100.0


def test_total_com_desconto():
    resultado = apply_coupon("DEVOPS10", 250.0)

    assert resultado["discount"] == 25.0
    assert resultado["total"] == 225.0

def test_cupom_vazio_e_invalido():
    assert apply_coupon("", 100.0)["valid"] is False
    assert apply_coupon(None, 100.0)["valid"] is False


def test_cupom_aceita_minusculas_e_espacos():
    resultado = apply_coupon("  devops10 ", 100.0)

    assert resultado["valid"] is True
    assert resultado["code"] == "DEVOPS10"