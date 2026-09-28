from app.features.coupon.service import apply_coupon, status


def test_status():
    assert status() == {"feature": "coupon", "status": "ok"}


def test_cupom_desconhecido_devolve_mensagem_amigavel_e_nao_altera_total():
    resultado = apply_coupon("CUPOMFALSO", 100.0)

    assert resultado["valid"] is False
    assert resultado["discount"] == 0.0
    assert resultado["total"] == 100.0
    assert "Cupom não encontrado" in resultado["message"]


def test_devops10_aplica_10_por_cento_de_desconto():
    resultado = apply_coupon("DEVOPS10", 200.0)

    assert resultado["valid"] is True
    assert resultado["discount"] == 20.0
    assert resultado["total"] == 180.0


def test_cupom_invalido_nao_altera_total_com_devops10_ativo():
    resultado = apply_coupon("DEVOPS99", 200.0)

    assert resultado["valid"] is False
    assert resultado["discount"] == 0.0
    assert resultado["total"] == 200.0