#!/bin/sh
set -e

echo "Running database migrations..."
python -m yoyo apply --database "sqlite:///${SQLITE_PATH}" ./migrations

echo "Starting Gunicorn..."
exec gunicorn "$APP_MODULE" \
  --bind "0.0.0.0:${PORT:-5000}" \
  --workers "$GUNICORN_WORKERS" \
  --timeout "$GUNICORN_TIMEOUT" \
  --access-logfile - \
  --error-logfile -