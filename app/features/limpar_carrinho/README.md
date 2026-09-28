# 025 - Botao Limpar Carrinho

Adiciona um botao "Limpar Carrinho" na pagina do carrinho (`/cart`), que remove
todos os itens do carrinho da sessao do usuario em uma unica acao.

## Como funciona

- O botao e injetado no slot `CART_SUMMARY` do template `cart.html` (core),
  via `SlotContribution` declarado em `manifest.py`.
- O botao envia um `POST` para `/limpar-carrinho/executar`.
- A rota chama `CarrinhoCleanerService.limpar()`, que esvazia
  `session["cart"]` (o mesmo dicionario usado por `app/core/routes/web.py`).
- O usuario e redirecionado de volta para `/cart` (padrao Post-Redirect-Get).

Nenhum arquivo de `app/core` foi alterado.
