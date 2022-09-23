""" Development Settings
"""

from dotenv import load_dotenv

# load environment variables from .env
load_dotenv()

from .settings import *  # noqa


DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),  # noqa: F405
    }
}

AUTH_PASSWORD_VALIDATORS = []

# Disable async mongo updates
MONGODB_ASYNC_SAVE = False
# Enable captcha test mode (use PASSED)
CAPTCHA_TEST_MODE = True
