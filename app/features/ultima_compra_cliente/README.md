# Última Compra Cliente

Feature responsável por identificar a compra mais recente de cada cliente,
conforme o Requisito 097 / Issue #62.

A regra de negócio consulta os pedidos associados ao nome do cliente, ordena
os resultados pela data de criação em ordem decrescente e retorna o pedido
mais recente. Caso o cliente não possua pedidos, o resultado é `None`.

## Testes

A feature possui testes para:

- cliente sem pedidos;
- cliente com um pedido;
- cliente com vários pedidos, validando a seleção do mais recente e o filtro
  pelo cliente.

A implementação está isolada em `app/features/ultima_compra_cliente`, sem
alteração do `app/core`.
