COUPONS = {
    "DEVOPS10": 0.10,
}


def status() -> dict[str, str]:
    return {"feature": "coupon", "status": "ok"}


def apply_coupon(code: str, total: float) -> dict:
    code = (code or "").strip().upper()
    rate = COUPONS.get(code)

    if rate is None:
        return {
            "valid": False,
            "code": code,
            "discount": 0.0,
            "total": total,
            "message": "Cupom não encontrado. Confira o código e tente novamente.",
        }

    discount = round(total * rate, 2)
    return {
        "valid": True,
        "code": code,
        "discount": discount,
        "total": round(total - discount, 2),
        "message": f"Cupom {code} aplicado: desconto de {rate:.0%}.",
    }