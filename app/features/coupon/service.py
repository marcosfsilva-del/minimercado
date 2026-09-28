def status() -> dict[str, str]:
    return {"feature": "coupon", "status": "ok"}


def apply_coupon(code: str, total: float) -> dict:
    code = (code or "").strip().upper()
    return {
        "valid": False,
        "code": code,
        "discount": 0.0,
        "total": total,
        "message": "Cupom não encontrado. Confira o código e tente novamente.",
    }