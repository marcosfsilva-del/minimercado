from app.core.app_factory import create_app


def test_readiness_endpoint_retorna_ready_em_json():
    """
    Issue #19 — Requisito 103: Endpoint Readiness.
    Verifica os três critérios de aceite:
    - retorna 'ready' quando a aplicação pode receber tráfego;
    - resposta em formato JSON;
    - status HTTP 200 quando pronta.
    """
    app = create_app()
    client = app.test_client()

    response = client.get("/readiness")

    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert response.get_json() == {"status": "ready"}