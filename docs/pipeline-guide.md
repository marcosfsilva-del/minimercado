# Guia De Pipeline

O projeto entrega comandos, testes e Docker. Não entrega CI pronta.

Requisitos minimos da pipeline do aluno:

```text
CHECKOUT
   ↓
INSTALACAO
   ↓
LINT
   ↓
TESTES
   ↓
BUILD
```

Comandos sugeridos:

```bash
python3 -m pip install -r requirements-dev.txt
python3 tasks.py lint
python3 tasks.py test
python3 tasks.py build
```

Depois a mesma pipeline evolui para Docker, registry, deploy preview e smoke test.
