"""Lógica de negócio do endpoint de readiness."""


def check_readiness() -> dict:
    """
    Verifica se a aplicação está pronta para receber tráfego.

    Retorna um dicionário serializável em JSON com o status.
    """
    
    return {"status": "ready"}