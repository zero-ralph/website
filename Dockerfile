# --- Stage 1: Build & Sync dependencies ---
FROM python:3.14-slim-bookworm AS builder

# Copy the uv binary directly from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies needed for compiling packages (e.g., psycopg)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies using cache mounts for extreme speed
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

# --- Stage 2: Clean Production Runtime ---
FROM python:3.14-slim-bookworm AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# Install runtime library for PostgreSQL
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Create and switch to a secure, non-root system user
RUN groupadd -r appuser && useradd -r -m -g appuser appuser

# Copy the isolated virtual environment from the builder
COPY --from=builder --chown=appuser:appuser /app/.venv /app/.venv

# Copy your remaining Django application code
COPY --chown=appuser:appuser . .

USER appuser

EXPOSE 8000

# Production default command (Compose will override this for local development)
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
