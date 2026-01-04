# git
save:
	git add . && git commit -m "$(msg)"

run:
	poetry run python manage.py runserver

check:
	poetry run python manage.py check

shell:
	poetry run python manage.py shell

showmigrations:
	poetry run python manage.py showmigrations

newapp:
	poetry run python manage.py startapp $(name)

superuser-auto:
	./bash/new_superuser.sh

superuser:
	poetry run python manage.py createsuperuser

check-active-user:
	poetry run python manage.py dbshell 
# and then - SELECT current_user;

migrate:
	poetry run python manage.py makemigrations && poetry run python manage.py migrate && poetry run python manage.py runserver 

changepass:
	poetry run python manage.py changepassword $(user)

requirements:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

# postgresql
setup-postgres:
	./bash/setup_postgres.sh

# 1. Create .env file on production
# 2. Check for deploy-related issues
# 3. Collect static files
# 4. Apply database migrations

secret-key-prod:
	python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

env-prod:
	chmod +x ./bash/make_env_prod.sh && ./bash/make_env_prod.sh

deploy-check:
	python manage.py check --deploy --settings=jobs_portal.settings.prod

check-prod:
	python manage.py check --settings=jobs_portal.settings.prod

static-prod:
	python manage.py collectstatic --settings=jobs_portal.settings.prod --noinput

migrate-prod:
	python manage.py makemigrations --settings=jobs_portal.settings.prod && python manage.py migrate --settings=jobs_portal.settings.prod

superuser-prod:
	python manage.py createsuperuser --settings=jobs_portal.settings.prod

run-prod:
	python manage.py runserver --settings=jobs_portal.settings.prod

# Helpers
activate-venv-prod:
	source ~/.venvs/myvenv/bin/activate

# frontend
frontend-install:
	npm install jquery bootstrap @fortawesome/fontawesome-free

frontend-copy:
	cp node_modules/jquery/dist/jquery.min.js static/js/libs/ && cp node_modules/bootstrap/dist/css/bootstrap.min.css static/css/libs/ && cp node_modules/bootstrap/dist/css/bootstrap.min.css.map static/css/libs/ && cp -r node_modules/@fortawesome/fontawesome-free/webfonts static/ && cp node_modules/@fortawesome/fontawesome-free/css/all.min.css static/css/libs/ && cp node_modules/bootstrap/dist/js/bootstrap.min.js static/js/libs/

fix-webfonts:
	sed -i 's|\.\./webfonts|../../webfonts|g' static/css/libs/all.min.css

frontend:
	make frontend-install && make frontend-copy && make fix-webfonts && make run