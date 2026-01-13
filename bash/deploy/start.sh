#!/bin/sh
set -e

python manage.py check --deploy --settings=code_levels.settings.prod

python manage.py makemigrations --settings=code_levels.settings.prod
python manage.py migrate --settings=code_levels.settings.prod

python manage.py collectstatic --settings=code_levels.settings.prod --noinput

exec gunicorn code_levels.wsgi:application --bind 0.0.0.0:$PORT
