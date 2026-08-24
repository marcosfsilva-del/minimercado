from app.features.contador_no_menu.service import status


def test_status():
    assert status() == {"feature": "contador-no-menu", "status": "ok"}
