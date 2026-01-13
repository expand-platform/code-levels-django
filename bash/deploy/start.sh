#!/usr/bin/env bash
set -e

echo "Starting deploy script..."

echo "Running Django deploy checks..."
python manage.py check --deploy --settings=code_levels.settings.prod

echo "Applying migrations..."
python manage.py migrate --noinput --settings=code_levels.settings.prod

echo "Collecting static files..."
python manage.py collectstatic --noinput --settings=code_levels.settings.prod

echo "Starting Gunicorn..."
exec gunicorn code_levels.wsgi:application \
  --bind 0.0.0.0:$PORT \
  --workers 2 \
  --threads 4 \
  --timeout 60
