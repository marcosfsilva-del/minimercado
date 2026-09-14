from app.features.endpoint_readiness.service import status


def test_status():
    assert status() == {"feature": "endpoint-readiness", "status": "ok"}
