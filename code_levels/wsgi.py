import os
from django.core.wsgi import get_wsgi_application
from code_levels.settings.base import env

os.environ.setdefault('DJANGO_SETTINGS_MODULE', str(env("DJANGO_SETTINGS_MODULE")))

application = get_wsgi_application()
