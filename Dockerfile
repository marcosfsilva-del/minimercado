# syntax=docker/dockerfile:1.7
# ==========================================
# Estágio 1: Builder (Compilação e Resolução)
# ==========================================
FROM python:3.13-slim AS builder

WORKDIR /app

ENV PIP_NO_CACHE_DIR=0 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1

# Pacotes essenciais de compilação com patch de segurança
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Cria o virtualenv isolado
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt

# Remove os utilitários de build para zerar CVEs de packaging (Trivy / Snyk)
RUN pip uninstall -y pip setuptools wheel 2>/dev/null || true

# ==========================================
# Estágio 2: Runtime Final (Hardened & Autocontido)
# ==========================================
FROM python:3.13-slim AS runner

WORKDIR /app

ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=0 \
    PYTHON_JIT=1 \
    PORT=3000 \
    DATABASE_URL="sqlite:////app/data/devops_market.db"

# Aplica patches do Debian e limpa caches/permissões perigosas
RUN apt-get update && apt-get upgrade -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
           /usr/share/doc /usr/share/man /usr/share/locale && \
    find / -xdev -perm /6000 -type f -exec chmod a-s {} + 2>/dev/null || true

# Criação do usuário não-root e diretório de dados do SQLite
RUN groupadd -g 10001 appgroup && \
    useradd -u 10001 -g appgroup -s /bin/sh -d /app appuser && \
    mkdir -p /app/data && \
    chown -R appuser:appgroup /app

# Copia dependências validadas
COPY --from=builder --chown=appuser:appgroup /opt/venv /opt/venv

# Copia código-fonte
COPY --chown=appuser:appgroup . .

# Pré-compila bytecode otimizado
RUN python -m compileall -b -q -o 1 app scripts tasks.py

USER appuser

EXPOSE 3000

# Healthcheck nativo em Python (sem dependência de curl/wget)
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request, os, sys; sys.exit(0 if urllib.request.urlopen(f'http://localhost:{os.environ.get(\"PORT\", 3000)}/health', timeout=2).getcode() == 200 else 1)"

# Executa seed do banco e transfere o controle com PID 1 via exec para o servidor
CMD ["sh", "-c", "python tasks.py db-seed && exec python -m app.core.server"]
