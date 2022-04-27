"""
Django settings for mdcs project.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
from mongoengine.connection import connect

from core_main_app.utils.logger.logger_utils import (
    set_generic_handler,
    set_generic_logger,
    update_logger_with_local_app,
)
from .core_settings import *
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = (
    os.environ["DJANGO_SECRET_KEY"] if "DJANGO_SECRET_KEY" in os.environ else None
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = (
    os.environ["ALLOWED_HOSTS"].split(",") if "ALLOWED_HOSTS" in os.environ else []
)

# Databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": os.environ["POSTGRES_HOST"] if "POSTGRES_HOST" in os.environ else None,
        "PORT": int(os.environ["POSTGRES_PORT"])
        if "POSTGRES_PORT" in os.environ
        else 5432,
        "NAME": os.environ["POSTGRES_DB"] if "POSTGRES_DB" in os.environ else None,
        "USER": os.environ["POSTGRES_USER"] if "POSTGRES_USER" in os.environ else None,
        "PASSWORD": os.environ["POSTGRES_PASS"]
        if "POSTGRES_PASS" in os.environ
        else None,
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

MONGO_HOST = os.environ["MONGO_HOST"] if "MONGO_HOST" in os.environ else ""
MONGO_PORT = os.environ["MONGO_PORT"] if "MONGO_PORT" in os.environ else "27017"
MONGO_DB = os.environ["MONGO_DB"] if "MONGO_DB" in os.environ else ""
MONGO_USER = os.environ["MONGO_USER"] if "MONGO_USER" in os.environ else ""
MONGO_PASS = os.environ["MONGO_PASS"] if "MONGO_PASS" in os.environ else ""
MONGODB_URI = (
    f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
)
connect(host=MONGODB_URI, connect=False)


BROKER_TRANSPORT_OPTIONS = {
    "visibility_timeout": 3600,
    "fanout_prefix": True,
    "fanout_patterns": True,
}
REDIS_HOST = os.environ["REDIS_HOST"] if "REDIS_HOST" in os.environ else ""
REDIS_PORT = os.environ["REDIS_PORT"] if "REDIS_PORT" in os.environ else "6379"
REDIS_PASS = os.environ["REDIS_PASS"] if "REDIS_PASS" in os.environ else None

if REDIS_PASS:
    REDIS_URL = f"redis://:{REDIS_PASS}@{REDIS_HOST}:{REDIS_PORT}"
else:
    REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}"
BROKER_URL = REDIS_URL
CELERY_RESULT_BACKEND = REDIS_URL
CELERYBEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

# Application definition

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "oauth2_provider",
    # Extra apps
    "rest_framework",
    "drf_yasg",
    "rest_framework_mongoengine",
    "menu",
    "tz_detect",
    "defender",
    "captcha",
    "django_celery_beat",
    # Core apps
    "core_main_app",
    "core_exporters_app",
    "core_exporters_app.exporters.xsl",
    "core_website_app",
    "core_oaipmh_common_app",
    "core_oaipmh_harvester_app",
    "core_oaipmh_provider_app",
    "core_curate_app",
    "core_parser_app",
    "core_parser_app.tools.modules",  # FIXME: make modules an app
    "core_parser_app.tools.parser",  # FIXME: make parser an app
    "core_composer_app",
    "core_explore_federated_search_app",
    "core_federated_search_app",
    "core_explore_common_app",
    "core_explore_oaipmh_app",
    "core_explore_example_app",
    "core_explore_keyword_app",
    "core_dashboard_app",
    "core_dashboard_common_app",
    "core_file_preview_app",
    "core_linked_records_app",
    # modules
    "core_module_blob_host_app",
    "core_module_remote_blob_host_app",
    "core_module_advanced_blob_host_app",
    "core_module_excel_uploader_app",
    "core_module_periodic_table_app",
    "core_module_chemical_composition_app",
    "core_module_chemical_composition_simple_app",
    "core_module_text_area_app",
    # Local apps
    "mdcs_home",
)

MIDDLEWARE = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "defender.middleware.FailedLoginMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "tz_detect.middleware.TimezoneMiddleware",
)


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "core_main_app.utils.custom_context_processors.domain_context_processor",  # Needed by any curator app
                "django.template.context_processors.i18n",
            ],
        },
    },
]

ROOT_URLCONF = "mdcs.urls"

WSGI_APPLICATION = "mdcs.wsgi.application"


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = "static.prod"

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
)

STATICFILES_DIRS = ("static",)

# Password Validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 8,
        },
    },
    {
        "NAME": "core_main_app.commons.validators.UpperCaseLetterCountValidator",
        "OPTIONS": {
            "min_uppercase_letters": 1,
        },
    },
    {
        "NAME": "core_main_app.commons.validators.LowerCaseLetterCountValidator",
        "OPTIONS": {
            "min_lowercase_letters": 1,
        },
    },
    {
        "NAME": "core_main_app.commons.validators.NonAlphanumericCountValidator",
        "OPTIONS": {
            "min_nonalphanumeric_letters": 1,
        },
    },
    {
        "NAME": "core_main_app.commons.validators.DigitsCountValidator",
        "OPTIONS": {
            "min_digits": 1,
        },
    },
    {
        "NAME": "core_main_app.commons.validators.MaxOccurrenceCountValidator",
        "OPTIONS": {
            "max_occurrence": 5,
        },
    },
]

# Django REST Framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
    ),
}

# drf-yasg
SWAGGER_SETTINGS = {
    "exclude_namespaces": [],  # List URL namespaces to ignore
    "api_version": "1.1",  # Specify your API's version
    "api_path": "/",  # Specify the path to your API not a root level
    "enabled_methods": [  # Specify which methods to enable in Swagger UI
        "get",
        "post",
        "put",
        "patch",
        "delete",
    ],
    "api_key": "",  # An API key
    "is_authenticated": False,  # Set to True to enforce user authentication,
    "is_superuser": False,  # Set to True to enforce admin only access
    "LOGIN_URL": "core_main_app_login",
    "LOGOUT_URL": "core_main_app_logout",
}

# Django Defender
DEFENDER_REDIS_URL = REDIS_URL
""" :py:class:`str`: The Redis url for defender. 
"""
DEFENDER_COOLOFF_TIME = 60
""" integer: Period of inactivity after which old failed login attempts will be forgotten
"""
DEFENDER_LOGIN_FAILURE_LIMIT = 3
""" integer: The number of login attempts allowed before a record is created for the failed login.
"""
DEFENDER_STORE_ACCESS_ATTEMPTS = True
""" boolean: Store the login attempt to the database.
"""
DEFENDER_USE_CELERY = True
""" boolean: Use Celery to store the login attempt to the database.
"""
DEFENDER_LOCKOUT_URL = "/locked"
""" string: url to the defender error page (defined in core_main_app)
"""

# Django simple-menu
MENU_SELECT_PARENTS = False

# mdcs_home
HOMEPAGE_NB_LAST_TEMPLATES = 6
""" integer: How many templates are displayed on the homepage
"""

# Logging

LOGGING_SERVER = True
LOGGING_CLIENT = True
LOGGING_DB = True

LOGGER_FILE_SERVER = os.path.join(BASE_DIR, "logfile_server.txt")
LOGGER_FILE_CLIENT = os.path.join(BASE_DIR, "logfile_client.txt")
LOGGER_FILE_DB = os.path.join(BASE_DIR, "logfile_db.txt")
LOGGER_FILE_SECURITY = os.path.join(BASE_DIR, "logfile_security.txt")
LOGGER_FILE_APP = os.path.join(BASE_DIR, "logfile_app.txt")

LOGGER_LEVEL = os.getenv("DJANGO_LOG_LEVEL", "DEBUG")
LOGGER_CLIENT_LEVEL = os.getenv("DJANGO_LOG_LEVEL", "INFO")
LOGGER_SERVER_LEVEL = os.getenv("DJANGO_LOG_LEVEL", "DEBUG")
LOGGER_DB_LEVEL = os.getenv("DJANGO_LOG_LEVEL", "DEBUG")
LOGGER_APP_LEVEL = os.getenv("DJANGO_LOG_LEVEL", "DEBUG")

LOGGER_MAX_BYTES = 500000
LOGGER_BACKUP_COUNT = 2

local_logger_conf = {
    "handlers": ["app_handler", "console"],
    "level": LOGGER_APP_LEVEL,
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "fmt-default": {
            "format": "%(levelname)s: %(asctime)s\t%(name)s\t%(pathname)s\tl.%(lineno)s\t%(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "logfile-security": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOGGER_FILE_SECURITY,
            "maxBytes": LOGGER_MAX_BYTES,
            "backupCount": LOGGER_BACKUP_COUNT,
            "formatter": "fmt-default",
        },
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "fmt-default",
        },
        "app_handler": {
            "level": LOGGER_APP_LEVEL,
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOGGER_FILE_APP,
            "maxBytes": LOGGER_MAX_BYTES,
            "backupCount": LOGGER_BACKUP_COUNT,
            "formatter": "fmt-default",
        },
    },
    "loggers": {
        "django.security": {
            "handlers": ["console", "logfile-security"],
            "level": LOGGER_LEVEL,
            "propagate": True,
        },
    },
}

update_logger_with_local_app(LOGGING, local_logger_conf, INSTALLED_APPS)

if LOGGING_CLIENT:
    set_generic_handler(
        LOGGING,
        "logfile-template",
        LOGGER_CLIENT_LEVEL,
        LOGGER_FILE_CLIENT,
        LOGGER_MAX_BYTES,
        LOGGER_BACKUP_COUNT,
        "logging.handlers.RotatingFileHandler",
    )
    set_generic_logger(
        LOGGING, "django.template", LOGGER_CLIENT_LEVEL, ["console", "logfile-template"]
    )
    set_generic_handler(
        LOGGING,
        "logfile-request",
        LOGGER_CLIENT_LEVEL,
        LOGGER_FILE_CLIENT,
        LOGGER_MAX_BYTES,
        LOGGER_BACKUP_COUNT,
        "logging.handlers.RotatingFileHandler",
    )
    set_generic_logger(
        LOGGING, "django.request", LOGGER_CLIENT_LEVEL, ["console", "logfile-request"]
    )

if LOGGING_SERVER:
    set_generic_handler(
        LOGGING,
        "logfile-server",
        LOGGER_SERVER_LEVEL,
        LOGGER_FILE_SERVER,
        LOGGER_MAX_BYTES,
        LOGGER_BACKUP_COUNT,
        "logging.handlers.RotatingFileHandler",
    )
    set_generic_logger(
        LOGGING, "django.server", LOGGER_SERVER_LEVEL, ["console", "logfile-server"]
    )

if LOGGING_DB:
    set_generic_handler(
        LOGGING,
        "logfile-django-db-backend",
        LOGGER_DB_LEVEL,
        LOGGER_FILE_DB,
        LOGGER_MAX_BYTES,
        LOGGER_BACKUP_COUNT,
        "logging.handlers.RotatingFileHandler",
    )
    set_generic_logger(
        LOGGING,
        "django.db.backends",
        LOGGER_DB_LEVEL,
        ["console", "logfile-django-db-backend"],
    )


# SSL

if SERVER_URI.lower().startswith("https"):
    # Activate HTTPS
    os.environ["HTTPS"] = "on"

    # Secure cookies
    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_AGE = None
    SESSION_COOKIE_SECURE = True
    SESSION_EXPIRE_AT_BROWSER_CLOSE = True
    SESSION_COOKIE_AGE = 604800

    # Set x-frame options
    X_FRAME_OPTIONS = "SAMEORIGIN"

if ENABLE_SAML2_SSO_AUTH:
    import saml2
    import saml2.saml
    from core_main_app.utils.saml2.utils import (
        load_saml_config_from_env,
        load_django_attribute_map_from_env,
    )

    # Update Django Settings
    if "djangosaml2" not in INSTALLED_APPS:
        INSTALLED_APPS = INSTALLED_APPS + ("djangosaml2",)
    if "djangosaml2.middleware.SamlSessionMiddleware" not in MIDDLEWARE:
        MIDDLEWARE = MIDDLEWARE + ("djangosaml2.middleware.SamlSessionMiddleware",)
    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
        "djangosaml2.backends.Saml2Backend",
    )

    # Configure djangosaml2
    SAML_SESSION_COOKIE_NAME = "saml_session"
    LOGIN_REDIRECT_URL = "/"
    LOGOUT_REDIRECT_URL = "/"
    SAML_DEFAULT_BINDING = saml2.BINDING_HTTP_POST
    SAML_LOGOUT_REQUEST_PREFERRED_BINDING = saml2.BINDING_HTTP_POST
    SAML_IGNORE_LOGOUT_ERRORS = True
    SAML_DJANGO_USER_MAIN_ATTRIBUTE = os.getenv(
        "SAML_DJANGO_USER_MAIN_ATTRIBUTE", "username"
    )
    SAML_USE_NAME_ID_AS_USERNAME = (
        os.getenv("SAML_USE_NAME_ID_AS_USERNAME", "False").lower() == "true"
    )
    SAML_CREATE_UNKNOWN_USER = (
        os.getenv("SAML_CREATE_UNKNOWN_USER", "False").lower() == "true"
    )
    SAML_ATTRIBUTE_MAPPING = load_django_attribute_map_from_env()

    # Configure Pysaml2
    SAML_CONFIG = load_saml_config_from_env(server_uri=SERVER_URI, base_dir=BASE_DIR)
    SAML_ACS_FAILURE_RESPONSE_FUNCTION = "core_main_app.views.user.views.saml2_failure"

# configure handle server PIDs according to environment settings
if ENABLE_HANDLE_PID:
    HDL_USER = (
        f"300%3A{ID_PROVIDER_PREFIX_DEFAULT}/"
        f'{os.getenv("HANDLE_NET_USER", "ADMIN")}'
    )

    ID_PROVIDER_SYSTEM_NAME = "handle.net"
    ID_PROVIDER_SYSTEM_CONFIG = {
        "class": "core_linked_records_app.utils.providers.handle_net.HandleNetSystem",
        "args": [
            os.getenv("HANDLE_NET_LOOKUP_URL", "https://hdl.handle.net"),
            os.getenv("HANDLE_NET_REGISTRATION_URL", "https://handle-net.domain"),
            HDL_USER,
            os.getenv("HANDLE_NET_SECRET_KEY", "admin"),
        ],
    }

    HANDLE_NET_RECORD_INDEX = os.getenv("HANDLE_NET_RECORD_INDEX", 1)
    HANDLE_NET_ADMIN_DATA = {
        "index": int(os.getenv("HANDLE_NET_ADMIN_INDEX", 100)),
        "type": os.getenv("HANDLE_NET_ADMIN_TYPE", "HS_ADMIN"),
        "data": {
            "format": os.getenv("HANDLE_NET_ADMIN_DATA_FORMAT", "admin"),
            "value": {
                "handle": f"0.NA/{ID_PROVIDER_PREFIX_DEFAULT}",
                "index": int(os.getenv("HANDLE_NET_ADMIN_DATA_INDEX", 200)),
                "permissions": os.getenv(
                    "HANDLE_NET_ADMIN_DATA_PERMISSIONS", "011111110011"
                ),
            },
        },
    }
