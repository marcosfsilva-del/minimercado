# Repetir Compra

Issue #15 (requisito 073): botão "Repetir" no histórico de pedidos.

- `manifest.py` injeta o botão no slot `ORDER_SUMMARY` da tela de pedidos.
- `routes.py` recebe `POST /repeat-order/<order_id>` e redireciona para o carrinho.
- `service.py` copia os itens do pedido para o carrinho respeitando o estoque atual.
