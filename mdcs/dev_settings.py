""" Development Settings
"""

from dotenv import load_dotenv

# load environment variables from .env
load_dotenv()

from .settings import *  # noqa

# Run in debug mode in development
DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),  # noqa: F405
    }
}

# Remove constraint checks on passwords
AUTH_PASSWORD_VALIDATORS = []

# Disable async mongo updates
MONGODB_ASYNC_SAVE = False
# Enable captcha test mode (use PASSED)
CAPTCHA_TEST_MODE = True
# Run celery tasks in the main process
CELERY_ALWAYS_EAGER = True

# Django Allauth dev settings
MFA_WEBAUTHN_ALLOW_INSECURE_ORIGIN = True
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
ACCOUNT_EMAIL_VERIFICATION = "none"
