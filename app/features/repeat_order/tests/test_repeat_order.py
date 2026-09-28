import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.database import Base
from app.core.models import Product
from app.core.services.market_service import create_order
from app.features.repeat_order.service import repeat_order


@pytest.fixture()
def db():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine, expire_on_commit=False)()
    session.add_all(
        [
            Product(id=1, name="Arroz", description="d", category="c", price=10.0, stock=10),
            Product(id=2, name="Feijão", description="d", category="c", price=5.0, stock=10),
        ]
    )
    session.flush()
    yield session
    session.close()


def _order(db):
    items = [{"product_id": 1, "quantity": 3}, {"product_id": 2, "quantity": 2}]
    return create_order(db, items, "Gabriel")


def test_repeat_order_adds_items_with_original_quantities(db):
    order = _order(db)
    cart: dict[str, int] = {}

    result = repeat_order(db, order.id, cart)

    assert cart == {"1": 3, "2": 2}
    assert result == {"added": ["Arroz", "Feijão"], "adjusted": [], "unavailable": []}


def test_repeat_order_respects_current_stock(db):
    order = _order(db)  # estoque cai para 7 e 8
    db.get(Product, 1).stock = 2
    db.get(Product, 2).stock = 0
    cart: dict[str, int] = {}

    result = repeat_order(db, order.id, cart)

    assert cart == {"1": 2}
    assert result["adjusted"] == ["Arroz"]
    assert result["unavailable"] == ["Feijão"]


def test_repeat_order_unknown_order_raises(db):
    with pytest.raises(ValueError, match="Pedido não encontrado"):
        repeat_order(db, 999, {})


def test_repeat_button_route_fills_session_cart(db, monkeypatch):
    from contextlib import contextmanager

    from app.core import create_app

    order = _order(db)

    @contextmanager
    def fake_scope():
        yield db

    monkeypatch.setattr("app.features.repeat_order.routes.session_scope", fake_scope)
    client = create_app().test_client()

    response = client.post(f"/repeat-order/{order.id}")

    assert response.status_code == 302
    with client.session_transaction() as sess:
        assert sess["cart"] == {"1": 3, "2": 2}


def test_orders_page_shows_repeat_button(db, monkeypatch):
    from contextlib import contextmanager

    from app.core import create_app

    order = _order(db)

    @contextmanager
    def fake_scope():
        yield db

    monkeypatch.setattr("app.core.routes.web.session_scope", fake_scope)
    client = create_app().test_client()

    html = client.get("/orders").get_data(as_text=True)

    assert f'action="/repeat-order/{order.id}"' in html
    assert ">Repetir<" in html
