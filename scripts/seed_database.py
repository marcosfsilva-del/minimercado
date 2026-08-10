from app.core.database import init_database, session_scope
from app.core.models import Product

PRODUCTS = [
    ("Arroz", "Pacote de arroz branco 5kg", "Mercearia", 24.90, 30, True),
    ("Feijao", "Feijao carioca 1kg", "Mercearia", 8.49, 40, False),
    ("Cafe", "Cafe torrado e moido 500g", "Bebidas", 15.90, 25, True),
    ("Leite", "Leite integral 1L", "Laticinios", 4.79, 60, False),
    ("Acucar", "Acucar refinado 1kg", "Mercearia", 5.29, 35, False),
    ("Macarrao", "Macarrao espaguete 500g", "Massas", 3.99, 50, False),
    ("Sabonete", "Sabonete perfumado 90g", "Higiene", 2.49, 80, True),
    ("Detergente", "Detergente neutro 500ml", "Limpeza", 2.19, 70, False),
    ("Refrigerante", "Refrigerante cola 2L", "Bebidas", 8.99, 22, True),
    ("Biscoito", "Biscoito recheado 130g", "Mercearia", 3.49, 45, False),
]


def main() -> None:
    init_database()
    with session_scope() as db:
        for index, (name, description, category, price, stock, promotional) in enumerate(
            PRODUCTS, start=1
        ):
            product = db.get(Product, index)
            if product is None:
                product = Product(id=index)
                db.add(product)

            product.name = name
            product.description = description
            product.category = category
            product.price = price
            product.stock = stock
            product.promotional = promotional

    print("Seed concluído.")


if __name__ == "__main__":
    main()
