from typing import Any


def status() -> dict[str, str]:
    return {"feature": "product-search", "status": "ok"}


def search_products(products: list[Any], term: str | None) -> list[Any]:
    """Filtra produtos pelo nome contendo o termo de busca (case-insensitive)."""
    if not term or not term.strip():
        return list(products)

    normalized = term.strip().lower()
    matched = []
    for item in products:
        name = getattr(item, "name", None)
        if name is None and isinstance(item, dict):
            name = item.get("name", "")
        if name and normalized in str(name).lower():
            matched.append(item)
    return matched
