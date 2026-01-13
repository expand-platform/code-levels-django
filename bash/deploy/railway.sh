#!/bin/sh
set -e

python manage.py check --deploy --settings=code_levels.settings.prod
python manage.py collectstatic --settings=code_levels.settings.prod --noinput

python manage.py makemigrations --settings=code_levels.settings.prod
python manage.py migrate --settings=code_levels.settings.prod
