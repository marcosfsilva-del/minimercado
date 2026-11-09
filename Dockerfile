FROM python:3.12-slim AS builder

WORKDIR /app

# Atualiza pacotes do sistema operacional na etapa de build
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

COPY requirements-dev.txt requirements.txt ./
RUN python -m pip install --upgrade pip && python -m pip install --prefix=/install -r requirements.txt

COPY . .
RUN python -m compileall -q app scripts tasks.py

FROM python:3.12-slim

WORKDIR /app
ENV PORT=3000
ENV DATABASE_URL=sqlite:////data/devops_market.db

# Atualiza pacotes do sistema na imagem final para remover as CVEs apontadas pelo Trivy
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

COPY --from=builder /install /usr/local
COPY . .

RUN mkdir -p data

EXPOSE 3000
CMD ["sh", "-c", "python tasks.py db-seed && python -m app.core.server"]
