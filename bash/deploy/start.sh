#!/usr/bin/env bash
set -e

echo "Starting deploy script..."


echo "Applying migrations..."
python manage.py migrate --noinput --settings=code_levels.settings.prod

echo "Ensuring staticfiles directory exists..."
mkdir -p staticfiles

echo "Collecting static files..."
python manage.py collectstatic --noinput --settings=code_levels.settings.prod

echo "Starting Gunicorn..."
exec gunicorn code_levels.wsgi:application \
  --bind 0.0.0.0:$PORT \
  --workers 2 \
  --threads 4 \
  --timeout 60
