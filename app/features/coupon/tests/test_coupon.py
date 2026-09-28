from app.features.coupon.service import apply_coupon, status


def test_status():
    assert status() == {"feature": "coupon", "status": "ok"}


def test_cupom_desconhecido_devolve_mensagem_amigavel_e_nao_altera_total():
    resultado = apply_coupon("CUPOMFALSO", 100.0)

    assert resultado["valid"] is False
    assert resultado["discount"] == 0.0
    assert resultado["total"] == 100.0
    assert "Cupom não encontrado" in resultado["message"]