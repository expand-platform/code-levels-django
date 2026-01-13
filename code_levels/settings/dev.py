from .base import *
from code_levels.settings.allauth.dev import *

DEBUG = True

INSTALLED_APPS += [
    "django_browser_reload",
]
MIDDLEWARE += [
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]


ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Local DB config for development
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}
