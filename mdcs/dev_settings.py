""" Development Settings
"""

from dotenv import load_dotenv
# load environment variables from .env
load_dotenv()

from .settings import *


DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

