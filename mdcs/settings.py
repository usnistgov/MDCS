"""
Django settings for mdcs project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
import os

from mongoengine.connection import connect

from core_main_app.utils.logger.logger_utils import (
    set_generic_handler,
    set_generic_logger,
    update_logger_with_local_app,
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "<secret_key>"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

MENU_SELECT_PARENTS = False

CURATE_MENU_NAME = "Data Curation"

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
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    "defender.middleware.FailedLoginMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "tz_detect.middleware.TimezoneMiddleware",
)

ROOT_URLCONF = "mdcs.urls"

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

WSGI_APPLICATION = "mdcs.wsgi.application"

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = "static.prod"

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
)

STATICFILES_DIRS = ("static",)

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

MONGO_USER = "mgi_user"
MONGO_PASSWORD = "mgi_password"
DB_NAME = "mgi"
DB_SERVER = "localhost"
MONGODB_URI = (
    "mongodb://" + MONGO_USER + ":" + MONGO_PASSWORD + "@" + DB_SERVER + "/" + DB_NAME
)
connect(DB_NAME, host=MONGODB_URI)

# core_main_app settings
SERVER_EMAIL = ""
EMAIL_SUBJECT_PREFIX = ""
USE_EMAIL = False
ADMINS = [("admin", "admin@example.com")]
MANAGERS = [("manager", "moderator@example.com")]

USE_BACKGROUND_TASK = False
# FIXME: set a redis password in production
# REDIS_PASSWORD = 'redispass'
# REDIS_URL = 'redis://:' + REDIS_PASSWORD + '@localhost:6379/0'

REDIS_URL = "redis://localhost:6379/0"
BROKER_URL = REDIS_URL
BROKER_TRANSPORT_OPTIONS = {
    "visibility_timeout": 3600,
    "fanout_prefix": True,
    "fanout_patterns": True,
}
CELERY_RESULT_BACKEND = REDIS_URL

# core_website_app settings
SERVER_URI = "http://localhost:8000"

# Password settings for django.contrib.auth validators
# Specifies the minimum length for passwords.
PASSWORD_MIN_LENGTH = 5
# Specifies the minimum amount of required letters in a password.
PASSWORD_MIN_LETTERS = 0
# Specifies the minimum amount of required uppercase letters in a password.
PASSWORD_MIN_UPPERCASE_LETTERS = 0
# Specifies the minimum amount of required lowercase letters in a password.
PASSWORD_MIN_LOWERCASE_LETTERS = 0
# Specifies the minimum amount of required numbers in a password.
PASSWORD_MIN_NUMBERS = 0
# Specifies the minimum amount of required symbols in a password.
PASSWORD_MIN_SYMBOLS = 0
# Specifies the maximum amount of consecutive characters allowed in passwords.
PASSWORD_MAX_OCCURRENCE = None

# ===============================================
# Website configuration
# ===============================================
# Choose from:  black, black-light, blue, blue-light, green, green-light, purple, purple-light, red, red-light, yellow,
#               yellow-light
WEBSITE_ADMIN_COLOR = "yellow"

WEBSITE_SHORT_TITLE = "MDCS"

DATA_AUTO_PUBLISH = True

# Customization Label
CUSTOM_DATA = "Materials Data"
CUSTOM_TITLE = "Materials Data Curation System"
CUSTOM_SUBTITLE = "Part of the Materials Genome Initiative"
CUSTOM_NAME = "Curator"


DATA_SOURCES_EXPLORE_APPS = [
    "core_explore_federated_search_app",
    "core_explore_oaipmh_app",
]

# FIXME: set desired value before release
# Lists in data not stored if number of elements is over the limit (e.g. 100)
SEARCHABLE_DATA_OCCURRENCES_LIMIT = None

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

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
    ),
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # )
}

HOMEPAGE_NB_LAST_TEMPLATES = 6
""" integer: How many templates is displayed on the homepage
"""

PARSER_DOWNLOAD_DEPENDENCIES = True
""" boolean: Does the parser download dependencies
"""

EXPLORE_ADD_DEFAULT_LOCAL_DATA_SOURCE_TO_QUERY = True
""" boolean: Do we add the local data source to new queries by default
"""

SSL_CERTIFICATES_DIR = True
""" Either a boolean, in which case it controls whether requests verify the server's TLS certificate, 
or a string, in which case it must be a path to a CA bundle to use.
"""

XSD_URI_RESOLVER = "REQUESTS_RESOLVER"
""" :py:class:`str`: XSD URI Resolver for lxml validation. Choose from:  None, 'REQUESTS_RESOLVER'.
"""

# Configure Django Defender
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
DISPLAY_EDIT_BUTTON = True
""" boolean: Display the edit button on the result page
"""
DATA_SORTING_FIELDS = ["-last_modification_date"]
""" Array<string>: Default sort fields for the data query. 
"""
DATA_DISPLAYED_SORTING_FIELDS = [
    {
        "field": "last_modification_date",
        "display": "Last updated",
        "ordering": "-last_modification_date",
    },
    {
        "field": "last_modification_date",
        "display": "First updated",
        "ordering": "+last_modification_date",
    },
    {"field": "title", "display": "Titles (A-Z)", "ordering": "+title"},
    {"field": "title", "display": "Titles (Z-A)", "ordering": "-title"},
    {"field": "template", "display": "Templates", "ordering": "+template"},
]
"""The default sorting fields displayed on the GUI, Data model field Array"""
SORTING_DISPLAY_TYPE = "single"
"""Result sorting graphical display type ('multi' / 'single')"""
DEFAULT_DATE_TOGGLE_VALUE = True
""" boolean: Set the toggle default value in the records list
"""
DISPLAY_PRIVACY_POLICY_FOOTER = False
""" boolean: display the privacy policy link in the footer
"""
DISPLAY_TERMS_OF_USE_FOOTER = True
""" boolean: display the terms of use link in the footer
"""
DISPLAY_CONTACT_FOOTER = False
""" boolean: display the contact link in the footer
"""
DISPLAY_HELP_FOOTER = False
""" boolean: display the help link in the footer
"""
DISPLAY_RULES_OF_BEHAVIOR_FOOTER = False
""" boolean: display the rules of behavior link in the footer
"""

ID_PROVIDER_SYSTEMS = {
    "local": {
        "class": "core_linked_records_app.utils.providers.local.LocalIdProvider",
        "args": [],
    },
    # "handle": {
    #     "class": "core_linked_records_app.utils.providers.handle_net.HandleNetSystem",
    #     "args": [
    #         "https://handle-server.example.org:8000",
    #         "300%3APREFIX/USER",
    #         "password",
    #     ],
    # },
}
""" dict: provider systems available for registring PIDs.
"""

ID_PROVIDER_PREFIXES = ["cdcs"]
""" list<str>: accepted providers if manually specifying PIDs (first item is the
default prefix)
"""

PID_XPATH = "root.pid"
""" string: location of the PID in the document, specified as dot notation
"""

AUTO_SET_PID = False
""" boolean: enable the automatic pid generation for saved data.
"""
