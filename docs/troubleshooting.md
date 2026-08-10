# Troubleshooting

## Porta ocupada

```bash
PORT=3101 python3 tasks.py dev
```

## Ambiente virtual quebrado

```bash
rm -r .venv
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements-dev.txt
```

## Banco vazio

```bash
python3 tasks.py db-seed
```

## Feature não apareceu

Confira se existe `app/features/<slug>/manifest.py` exportando `manifest`.

## Docker não sobe

```bash
docker compose up --build
```
