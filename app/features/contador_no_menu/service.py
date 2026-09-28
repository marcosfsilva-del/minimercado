def total_items(cart: dict[str, int]) -> int:
    """Soma as quantidades de todos os itens do carrinho (não conta só produtos distintos)."""
    return sum(cart.values())