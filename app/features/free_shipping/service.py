FREE_SHIPPING_MINIMUM = 100.00
SHIPPING_FEE = 15.00


def status() -> dict[str, str]:
    return {"feature": "free-shipping", "status": "ok"}


def format_brl(value: float) -> str:
    text = f"R$ {value:,.2f}"
    return text.replace(",", "X").replace(".", ",").replace("X", ".")


def has_free_shipping(subtotal: float, minimum: float = FREE_SHIPPING_MINIMUM) -> bool:
    return subtotal >= minimum


def remaining_for_free_shipping(subtotal: float, minimum: float = FREE_SHIPPING_MINIMUM) -> float:
    return round(max(minimum - subtotal, 0.0), 2)


def shipping_fee(subtotal: float, minimum: float = FREE_SHIPPING_MINIMUM) -> float:
    return 0.0 if has_free_shipping(subtotal, minimum) else SHIPPING_FEE


def shipping_message(subtotal: float, minimum: float = FREE_SHIPPING_MINIMUM) -> str:
    if has_free_shipping(subtotal, minimum):
        return "Frete grátis!"
    missing = format_brl(remaining_for_free_shipping(subtotal, minimum))
    return f"Faltam {missing} para frete grátis."


def summary(subtotal: float) -> dict:
    return {
        "subtotal": subtotal,
        "minimum": FREE_SHIPPING_MINIMUM,
        "free_shipping": has_free_shipping(subtotal),
        "shipping_fee": shipping_fee(subtotal),
        "remaining": remaining_for_free_shipping(subtotal),
        "message": shipping_message(subtotal),
    }