from app.features.free_shipping.service import (
    FREE_SHIPPING_MINIMUM,
    has_free_shipping,
    remaining_for_free_shipping,
    shipping_fee,
    shipping_message,
    status,
)


def test_status():
    assert status() == {"feature": "free-shipping", "status": "ok"}


def test_purchase_below_minimum_pays_shipping():
    assert not has_free_shipping(80.0)
    assert shipping_fee(80.0) > 0


def test_purchase_at_or_above_minimum_has_free_shipping():
    assert has_free_shipping(FREE_SHIPPING_MINIMUM)
    assert has_free_shipping(150.0)
    assert shipping_fee(150.0) == 0.0


def test_remaining_amount_and_message_below_minimum():
    assert remaining_for_free_shipping(80.0) == 20.0
    assert shipping_message(80.0) == "Faltam R$ 20,00 para frete grátis."


def test_message_when_free():
    assert shipping_message(150.0) == "Frete grátis!"