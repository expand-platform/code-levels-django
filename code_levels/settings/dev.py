from .base import *
from code_levels.settings.allauth.dev import *

INSTALLED_APPS += [
    "django_browser_reload",
]
MIDDLEWARE += [
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]



DEBUG = True
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
