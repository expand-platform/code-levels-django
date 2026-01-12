#!/bin/sh
# Exit immediately if a command exits with a non-zero status
set -e

# Check Django production settings
python manage.py check --deploy --settings=code_levels.settings.prod

# Install frontend dependencies
npm install jquery bootstrap @fortawesome/fontawesome-free

# Ensure static directories exist
mkdir -p static/js/libs static/css/libs static/webfonts

# Copy frontend assets
cp node_modules/jquery/dist/jquery.min.js static/js/libs/
cp node_modules/bootstrap/dist/css/bootstrap.min.css static/css/libs/
cp node_modules/bootstrap/dist/css/bootstrap.min.css.map static/css/libs/
cp -r node_modules/@fortawesome/fontawesome-free/webfonts static/
cp node_modules/@fortawesome/fontawesome-free/css/all.min.css static/css/libs/
cp node_modules/bootstrap/dist/js/bootstrap.min.js static/js/libs/

# Fix webfonts path in FontAwesome CSS
sed -i 's|\../webfonts|../../webfonts|g' static/css/libs/all.min.css

# Collect static files
python manage.py collectstatic --settings=code_levels.settings.prod --noinput

# Run migrations (makemigrations is optional in production)
python manage.py makemigrations --settings=code_levels.settings.prod
python manage.py migrate --settings=code_levels.settings.prod

# Start Gunicorn server
# gunicorn code_levels.wsgi:application

#! https://railpack.com/getting-started railpack configuration (NOdeJS env variable for prod)