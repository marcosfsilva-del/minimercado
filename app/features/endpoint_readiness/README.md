# Endpoint Readiness

## Descrição

Feature que expõe um endpoint de _readiness_, usado para verificar se a
aplicação está pronta para receber tráfego. Implementada para o
**Requisito 103 (Issue #19)**.

Diferente de um _health check_ simples — que só confirma que o processo
está de pé — o endpoint de readiness informa se a aplicação está em
condições reais de atender requisições.

## Rota

| Método | Rota         | Descrição                                  |
| ------ | ------------ | ------------------------------------------ |
| GET    | `/readiness` | Retorna o status de prontidão da aplicação |

## Resposta

Quando a aplicação está pronta para receber tráfego:

**Status HTTP:** `200 OK`

```json
{
  "status": "ready"
}
```

**Content-Type:** `application/json`

## Critérios de aceite

- [x] O endpoint retorna `ready` quando a aplicação pode receber tráfego
- [x] O endpoint usa formato JSON
- [x] O endpoint está documentado (este arquivo)

## Testes

Os testes desta feature estão em `tests/test_endpoint_readiness.py` e
cobrem:

- a chamada HTTP ao endpoint `/readiness`, validando status code,
  `content-type` e corpo da resposta;
- a função de serviço `check_readiness()` isoladamente.

Para rodar apenas os testes desta feature:

```bash
python -m pytest app/features/endpoint_readiness/tests -v
```
