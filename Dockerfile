# syntax=docker/dockerfile:1.7
# ==========================================
# Estágio 1: Builder (Compilação & Dependências)
# ==========================================
FROM python:3.13-slim AS builder

WORKDIR /app

# Otimizações de compilação e isolamento
ENV PIP_NO_CACHE_DIR=0 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1

# Instala toolchain de compilação para pacotes C/Rust com limpeza imediata
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Cria o virtualenv isolado
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# BuildKit Cache Mount: downloads e builds de wheels são cacheados entre builds
COPY requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt

# ==========================================
# Estágio 2: Runtime Final (Minimal & Hardened)
# ==========================================
FROM python:3.13-slim AS runner

WORKDIR /app

# Ativação do JIT (introduzido no Python 3.13) e flags de produção
ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=0 \
    PYTHON_JIT=1 \
    PORT=3000 \
    DATABASE_URL="sqlite:////app/data/devops_market.db"

# Dependências mínimas de runtime (curl para o healthcheck nativo)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Cria usuário não-root com UID/GID estático
RUN groupadd -g 10001 appgroup && \
    useradd -u 10001 -g appgroup -s /bin/sh -d /app appuser && \
    mkdir -p /app/data && \
    chown -R appuser:appgroup /app

# Copia dependências pré-construídas
COPY --from=builder --chown=appuser:appgroup /opt/venv /opt/venv

# Copia código da aplicação
COPY --chown=appuser:appgroup . .

# Compila bytecode (.pyc) antecipadamente com otimização (elimina asserts desnecessários em prod)
RUN python -m compileall -b -q -o 1 app scripts tasks.py

# Scripts de inicialização
RUN chmod +x docker-entrypoint.sh

USER appuser

EXPOSE 3000

# Healthcheck nativo para orquestradores (Swarm / K8s / Compose)
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:${PORT}/health || exit 1

ENTRYPOINT ["/app/docker-entrypoint.sh"]
CMD ["python", "-m", "app.core.server"]
