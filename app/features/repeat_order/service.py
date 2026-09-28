from sqlalchemy.orm import Session

from app.core.models import Order


def repeat_order(db: Session, order_id: int, cart: dict[str, int]) -> dict[str, list[str]]:
    """Adiciona ao carrinho os itens de um pedido anterior.

    `cart` tem o mesmo formato usado pelo carrinho do core: {"<product_id>": quantidade}.
    A regra de estoque é a mesma do create_order: nunca passar de product.stock.
    """
    order = db.get(Order, order_id)
    if order is None:
        raise ValueError(f"Pedido não encontrado: {order_id}")

    added: list[str] = []
    adjusted: list[str] = []
    unavailable: list[str] = []

    for item in order.items:
        product = item.product
        key = str(product.id)
        in_cart = cart.get(key, 0)
        wanted = in_cart + item.quantity
        final = min(wanted, product.stock)

        if final <= in_cart:
            unavailable.append(product.name)
            continue

        cart[key] = final
        if final < wanted:
            adjusted.append(product.name)
        else:
            added.append(product.name)

    return {"added": added, "adjusted": adjusted, "unavailable": unavailable}
