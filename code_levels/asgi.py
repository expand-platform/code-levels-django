import os

from django.core.asgi import get_asgi_application
from code_levels.settings.base import env

os.environ.setdefault("DJANGO_SETTINGS_MODULE", str(env("DJANGO_SETTINGS_MODULE")))

application = get_asgi_application()
