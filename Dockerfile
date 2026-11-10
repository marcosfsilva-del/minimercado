ARG PYTHON_VERSION=3.14

FROM python:${PYTHON_VERSION}-slim AS builder

WORKDIR /app
COPY requirements.txt ./
RUN python -m pip install --upgrade pip \
    && python -m pip install --prefix=/install -r requirements.txt

FROM python:${PYTHON_VERSION}-slim

RUN apt-get update \
    && apt-get upgrade -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
ENV PORT=3000
ENV DATABASE_URL=sqlite:///data/devops_market.db

COPY --from=builder /install /usr/local
COPY . .

RUN python -m pip uninstall -y pip setuptools || true \
    && mkdir -p data

EXPOSE 3000
CMD ["sh", "-c", "python tasks.py db-seed && python -m app.core.server"]
