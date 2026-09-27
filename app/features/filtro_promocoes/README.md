# Filtro de Promoções

Feature da issue #10 (requisito 013): filtro que mostra apenas produtos promocionais.

## Como funciona

- `service.list_promotional_products(session)` busca só os produtos com
  `promotional = True`, ordenados por nome (mesma ordem do catálogo).
- A rota `GET /promocoes` renderiza `templates/filtro-promocoes.html` com esses produtos.
- A rota `GET /promocoes/api` devolve a mesma lista em JSON.
- O `manifest.py` registra a ação "Ver promoções" em dois lugares sem tocar no core:
  - menu principal (`MenuItem`);
  - barra de ferramentas do catálogo, via slot `PRODUCT_LIST_TOOLBAR`.
- A tela de promoções tem o link "Voltar ao catálogo" para o catálogo completo.

## Critérios de aceitação

- [x] existe ação "ver promoções" (`test_existe_acao_ver_promocoes`)
- [x] apenas produtos promocionais aparecem (`test_apenas_produtos_promocionais_aparecem`)
- [x] usuário consegue voltar ao catálogo completo (`test_usuario_volta_ao_catalogo_completo`)

## Testes

```bash
python tasks.py test
```

Os testes usam um SQLite temporário por teste (`tests/conftest.py`), então não tocam
no banco de desenvolvimento em `data/`.
