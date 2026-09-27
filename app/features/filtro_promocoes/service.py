from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.models import Product


def list_promotional_products(session: Session) -> list[Product]:
    return list(
        session.scalars(
            select(Product).where(Product.promotional.is_(True)).order_by(Product.name)
        )
    )


def promotional_product_to_dict(product: Product) -> dict[str, object]:
    return {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "category": product.category,
        "price": product.price,
        "stock": product.stock,
        "promotional": product.promotional,
    }
