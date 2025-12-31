"""
WSGI config for code_levels project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from code_levels.settings.base import env

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'code_levels.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', str(env("DJANGO_SETTINGS_MODULE")))

application = get_wsgi_application()
