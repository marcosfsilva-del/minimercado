# Criando Uma Feature

```bash
python3 tasks.py feature-create product-search
python3 tasks.py feature-check product-search
```

Esse comando cria o pacote `app/features/product_search`, mantendo o id e a URL como `product-search`.

Depois:

1. Edite `manifest.py`.
2. Implemente rotas em `routes.py`.
3. Implemente regras em `service.py`.
4. Crie templates, se houver tela.
5. Escreva testes.
6. Rode lint, testes, build e smoke.
