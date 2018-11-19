"""
Django settings for mdcs project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
import os

from mongoengine.connection import connect
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '<secret_key>'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

MENU_SELECT_PARENTS = False

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'oauth2_provider',

    # Extra apps
    "password_policies",
    "rest_framework",
    "rest_framework_swagger",
    "rest_framework_mongoengine",
    "menu",
    "tz_detect",

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

    # modules
    "core_module_blob_host_app",
    "core_module_excel_uploader_app",
    "core_module_periodic_table_app",
    "core_module_chemical_composition_app",
    "core_module_text_area_app",

    # Local apps
    "mdcs_home"
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'tz_detect.middleware.TimezoneMiddleware',
    # 'password_policies.middleware.PasswordChangeMiddleware',
)

ROOT_URLCONF = 'mdcs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "core_main_app.utils.custom_context_processors.domain_context_processor",  # Needed by any curator app
                "django.template.context_processors.i18n",
            ],
        },
    },
]

WSGI_APPLICATION = 'mdcs.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static.prod'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

STATICFILES_DIRS = (
    'static',
)

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "logfile"),
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        '': {  # use 'MYAPP' to make it app specific
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
    }
}

MONGO_USER = "mgi_user"
MONGO_PASSWORD = "mgi_password"
DB_NAME = "mgi"
DB_SERVER = "localhost"
MONGODB_URI = "mongodb://" + MONGO_USER + ":" + MONGO_PASSWORD + "@" + DB_SERVER + "/" + DB_NAME
connect(DB_NAME, host=MONGODB_URI)

# core_main_app settings
SERVER_EMAIL = ""
EMAIL_SUBJECT_PREFIX = ""
USE_EMAIL = False
ADMINS = [('admin', 'admin@curator.org')]
MANAGERS = [('manager', 'moderator@curator.org')]

USE_BACKGROUND_TASK = False
BROKER_URL = 'redis://localhost:6379/0'
BROKER_TRANSPORT_OPTIONS = {
    'visibility_timeout': 3600,
    'fanout_prefix': True,
    'fanout_patterns': True
}
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# core_website_app settings
SERVER_URI = "http://localhost:8000"

# Password Policy
# Determines wether to use the password history.
PASSWORD_USE_HISTORY = False
# A list of raw strings representing paths to ignore while checking if a user has to change his/her password.
PASSWORD_CHANGE_MIDDLEWARE_EXCLUDED_PATHS = []
# Specifies the number of user's previous passwords to remember when the password history is being used.
# PASSWORD_HISTORY_COUNT = 1
# Determines after how many seconds a user is forced to change his/her password.
# PASSWORD_DURATION_SECONDS = 24 * 90 * 3600
# Don't log the person out in the middle of a session. Only do the checks at login time.
PASSWORD_CHECK_ONLY_AT_LOGIN = True
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
# Specifies a list of common sequences to attempt to match a password against.
# PASSWORD_COMMON_SEQUENCES = [u'0123456789', u'`1234567890-=', u'~!@#$%^&*()_+', u'abcdefghijklmnopqrstuvwxyz',
#                             u"quertyuiop[]\\asdfghjkl;'zxcvbnm,./", u'quertyuiop{}|asdfghjkl;"zxcvbnm<>?',
#                             u'quertyuiopasdfghjklzxcvbnm', u"1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik,9ol.0p;/-['=]\\",
#                             u'qazwsxedcrfvtgbyhnujmikolp']
PASSWORD_COMMON_SEQUENCES = []
# A minimum distance of the difference between old and new password. A positive integer.
# Values greater than 1 are recommended.
PASSWORD_DIFFERENCE_DISTANCE = 0
# Specifies the maximum amount of consecutive characters allowed in passwords.
PASSWORD_MAX_CONSECUTIVE = 10
# A list of project specific words to check a password against.
PASSWORD_WORDS = []

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


DATA_SOURCES_EXPLORE_APPS = ['core_explore_federated_search_app', 'core_explore_oaipmh_app']

# FIXME: set desired value before release
# Lists in data not stored if number of elements is over the limit (e.g. 100)
SEARCHABLE_DATA_OCCURRENCES_LIMIT = None

SWAGGER_SETTINGS = {
    "exclude_namespaces": [],  # List URL namespaces to ignore
    "api_version": '1.1',  # Specify your API's version
    "api_path": "/",  # Specify the path to your API not a root level
    "enabled_methods": [  # Specify which methods to enable in Swagger UI
        'get',
        'post',
        'put',
        'patch',
        'delete'
    ],
    "api_key": '',  # An API key
    "is_authenticated": False,  # Set to True to enforce user authentication,
    "is_superuser": False,  # Set to True to enforce admin only access
    'LOGIN_URL': 'core_main_app_login',
    'LOGOUT_URL': 'core_main_app_logout',
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
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

SSL_CERTIFICATES_DIR = 'certs'
""" :py:class:`str`: SSL certificates directory location.
"""