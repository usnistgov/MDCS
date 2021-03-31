""" Development Settings
"""

from dotenv import load_dotenv

# load environment variables from .env
load_dotenv()

from .settings import *


DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

AUTH_PASSWORD_VALIDATORS = []
