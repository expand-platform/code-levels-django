import environ

env = environ.Env()

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]


SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": env("GOOGLE_AUTH_CLIENT_ID", default=""),
            "secret": env("GOOGLE_AUTH_CLIENT_SECRET", default=""),
            "key": "",
        },
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        "OAUTH_PKCE_ENABLED": True,
        "SCOPE": [
            "profile",
            "email",
        ],
        "LOGIN_HINT": "",
        "PROMPT": "select_account",
        "SKIP_CONFIRMATION": True,
    }
}

ACCOUNT_FORMS = {
    "login": "platform_web.forms.CustomLoginForm",
    "signup": "platform_web.forms.custom_signup_form.CustomSignupForm",
    "socialaccount_signup": "platform_web.forms.custom_social_signup_form.CustomSocialSignupForm",
}

# Django auth settings
SITE_ID = 1
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_REDIRECT_URL = "home"
