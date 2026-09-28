def out_of_stock_label(stock: int) -> str | None:
    if stock <= 0:
        return "Esgotado"
    return None
