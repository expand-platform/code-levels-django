from pathlib import Path

from .base import *
from code_levels.settings.allauth.prod import *
from dj_database_url import parse

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = False
ROOT_URLCONF = "code_levels.urls"

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    *MIDDLEWARE[1:],
]

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    }
}

DATABASES = {
    "default": parse(
        env("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True,
    )
}


CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS")

SESSION_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
