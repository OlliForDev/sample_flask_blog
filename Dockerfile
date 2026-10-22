FROM python:3.13-slim

# uv aus dem offiziellen Image übernehmen
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/src \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# Zuerst nur die Abhängigkeitsdefinitionen kopieren
COPY pyproject.toml uv.lock ./

# Laufzeitabhängigkeiten aus dem Lockfile installieren
RUN uv sync --locked --no-dev --no-install-project --no-cache

# Anwendungscode und Migrationen kopieren
COPY src/blog ./src/blog
COPY migrations ./migrations

EXPOSE 5000

CMD ["uv", "run", "flask", "--app", "blog.app:create_app", "run", "--host=0.0.0.0", "--port=5000"]
