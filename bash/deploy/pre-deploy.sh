#!/usr/bin/env bash
set -e

echo "Starting deploy script..."

echo "Applying migrations..."
python manage.py migrate --noinput --settings=code_levels.settings.prod
q
echo "Ensuring staticfiles directory exists..."
mkdir -p staticfiles

echo "Collecting static files..."
python manage.py collectstatic --noinput --settings=code_levels.settings.prod