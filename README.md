# DevOps Market Python

Mini mercado web para a disciplina de Integracao DevOps, feito em Python para facilitar execucao em laboratorio.

O frontend usa Flask + Jinja. O backend usa Flask API. O banco e SQLite com SQLAlchemy.

## Primeira execucao

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements-dev.txt
python3 tasks.py db-seed
python3 tasks.py dev
```

Acesse `http://localhost:3000`.

## Comandos base para CI dos alunos

```bash
python3 -m pip install -r requirements-dev.txt
python3 tasks.py lint
python3 tasks.py test
python3 tasks.py build
python3 tasks.py docker-build
python3 tasks.py smoke
```

O comando `build` em Python faz uma construcao/validacao com `compileall`, garantindo que o codigo importa e compila para bytecode. O Dockerfile tambem tem um stage `builder`.

## Docker

```bash
docker compose up --build
```

Para preview em outra porta:

```bash
PORT=3101 docker compose up --build
```

## Features

```bash
python3 tasks.py feature-create product-search
python3 tasks.py feature-check product-search
```

Cada feature fica em um pacote Python. Slugs com hifen viram pasta com underscore.

```text
app/features/product_search/
  manifest.py
  routes.py
  service.py
  templates/
  tests/
  README.md
```

## Core protegido

Nao altere `app/core/*` para implementar uma feature comum. O aluno deve trabalhar em `app/features/<slug>`.

## CI

Este esqueleto nao entrega workflow pronto. Cada aluno cria sua propria pipeline na branch, em `.github/workflows/<nome-do-aluno-ou-feature>.yml`, usando os comandos base acima.
