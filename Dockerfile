# syntax=docker/dockerfile:1.7
# ==========================================
# Estágio 1: Builder (Compilação e Resolução)
# ==========================================
FROM python:3.13-alpine AS builder

WORKDIR /app

ENV PIP_NO_CACHE_DIR=0 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1

# Instala ferramentas necessárias para compilar wheels nativos no Alpine
RUN apk update && apk upgrade && apk add --no-cache \
    build-base \
    gcc \
    musl-dev \
    linux-headers

# Cria o virtualenv isolado
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade "pip>=26.3" "setuptools>=78.1.1" "wheel>=0.48.0" && \
    pip install -r requirements.txt

# Remove utilitários de packaging para não deixar vestígios para o scanner
RUN pip uninstall -y pip setuptools wheel 2>/dev/null || true

# ==========================================
# Estágio 2: Runtime Final (Minimal Zero-CVE)
# ==========================================
FROM python:3.13-alpine AS runner

WORKDIR /app

ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=0 \
    PYTHON_JIT=1 \
    PORT=3000 \
    DATABASE_URL="sqlite:////app/data/devops_market.db"

# Aplica patches de segurança do Alpine e remove o pip/setuptools da imagem base
RUN apk update && apk upgrade --no-cache && \
    rm -rf /var/cache/apk/* /tmp/* /var/tmp/* && \
    find /usr/local/lib/python3.13 -name "pip*" -exec rm -rf {} + 2>/dev/null || true && \
    find /usr/local/lib/python3.13 -name "setuptools*" -exec rm -rf {} + 2>/dev/null || true

# Criação do usuário não-root e diretório seguro do SQLite
RUN addgroup -g 10001 -S appgroup && \
    adduser -u 10001 -S appuser -G appgroup -h /app && \
    mkdir -p /app/data && \
    chown -R appuser:appgroup /app

# Copia apenas os pacotes instalados e validados do builder
COPY --from=builder --chown=appuser:appgroup /opt/venv /opt/venv

# Copia o código da aplicação
COPY --chown=appuser:appgroup . .

# Pré-compilação do bytecode
RUN python -m compileall -b -q -o 1 app scripts tasks.py

USER appuser

EXPOSE 3000

# Healthcheck nativo em Python
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request, os, sys; sys.exit(0 if urllib.request.urlopen(f'http://localhost:{os.environ.get(\"PORT\", 3000)}/health', timeout=2).getcode() == 200 else 1)"

CMD ["sh", "-c", "python tasks.py db-seed && exec python -m app.core.server"]
