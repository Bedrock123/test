import datetime
import os

from django.utils.encoding import smart_str

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# Base Django Time Zone Config
LANGUAGE_CODE = 'en'
TIME_ZONE = 'America/New_York'
USE_TZ = True
USE_I18N = False
USE_L10N = False
USE_I18N = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.environ.get('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    str(os.environ.get('ALLOWED_HOST_URL')),
]


# Application definition
DEFAULT_APPS = [
    'HarperUser',  # Custom User Model
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

]

THIRD_PARTY_APPS = [
    'easy_thumbnails',  # Allows you to put template image size tags
    'filer',  # Django Filer (Admin Side File Management)
    'mptt',  # Filer Dependencie
    'allauth',  # Django All Auth
    'allauth.account',  # Django All Auth Accounts
    'raven.contrib.django.raven_compat',  # Allows us to send data to
    'anymail',  # Supports our third party mail apps (Mail Gun)
    'autofixture',  # Creates fake data
    'widget_tweaks',  # Adds functionality to inject classes and such to django forms
    'versatileimagefield',  # ALlows user to upload image and to render crop functions on ti
    'robots',  # Automatically created a robots.txt file based on model rules
    'hijack',  # Allows admin to log in as a certain user, added it to core django project to override tempaltetags
    'compat',  # ^
    'hijack_admin',  # Allows admin to hijack users from the admin
    'webpack_loader',  # Allows Django to find the webpack bundle
    'rest_framework',  # Django REST Framework
    'corsheaders',  # alls for Cross Resours Shareing
    'storages',  # AWS Congifiration
    'logging',  # Allows AWS EC2 Server to Log Django Logs
    'opbeat.contrib.django',  # Error Lgging and Performance Monitoring
    'crispy_forms',  # Makes Plan Django Forms Pretty
    'captcha',
    'django_activeurl',
 
]

LOCAL_APPS = [
    'HarperStatic',
    'BaskingRidgeFiles'


]

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'opbeat.contrib.django.middleware.OpbeatAPMMiddleware',
    'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware',
    'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


CORS_ORIGIN_WHITELIST = (
    'localhost:3000',

)

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ROOT_URLCONF = 'BaskingRidge.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "HarperStatic", "templates"),
            os.path.join(BASE_DIR, "HarperStatic", "templates", "common"),
            os.path.join(BASE_DIR, "HarperStatic", "templates", "app"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
              
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'BaskingRidge.wsgi.application'


if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': str(os.environ['RDS_DB_NAME']),
            'USER': str(os.environ['RDS_USERNAME']),
            'PASSWORD': str(os.environ['RDS_PASSWORD']),
            'HOST': str(os.environ['RDS_HOSTNAME']),
            'PORT': str(os.environ['RDS_PORT'])
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Page Cache-Control
PAGE_CACHE_SECONDS = 6048000


# SETTING CUSTOM USER MODEL
AUTH_USER_MODEL = 'HarperUser.User'

# SITE_ID CONFIG
SITE_ID = 1

# ALL_AUTH SETTINGS
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_SIGNUP_FORM_CLASS = 'HarperUser.forms.AllauthSignupForm'

# Recapta Forms
RECAPTCHA_PUBLIC_KEY = '6Le_NSkUAAAAACpaOiRowk_n4xkyblqY4AS6JI7p'
RECAPTCHA_PRIVATE_KEY = '6Le_NSkUAAAAADoz-pWCAbOMjk-BDw14J2bEfnbc'
RECAPTCHA_PROXY = 'http://127.0.0.1:8000'
RECAPTCHA_USE_SSL = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')


STATIC_ROOT = os.path.join(BASE_DIR, "..", "www", "static")
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "HarperStatic", "static"),
)

# CSRF Failure View
CSRF_FAILURE_VIEW = 'BaskingRidge.urls.csrf_failure'

# Amazon Web Services S3 Settings & Configuration
AWS_ACCESS_KEY_ID = str(os.environ.get('AWS_ACCESS_KEY_ID'))
AWS_SECRET_ACCESS_KEY = str(os.environ.get('AWS_SECRET_ACCESS_KEY'))

AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True

DEFAULT_FILE_STORAGE = 'BaskingRidge.utils.MediaRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'avdplatformdev'
S3DIRECT_REGION = 'us-west-2'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = {
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}

# Django Compressor
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

)
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_ENABLED = True

# Twilio Backend
ACCOUNT_SID = str(os.environ.get('ACCOUNT_SID'))
AUTH_TOKEN = str(os.environ.get('AUTH_TOKEN'))
TWILIO_SENDER_KEY = str(os.environ.get('TWILIO_SENDER_KEY'))

# Once you get on AWS, just change it over to GMAIL :/
ANYMAIL = {
    "SENDGRID_API_KEY": str(os.environ.get('SENDGRID_API_KEY')),
}
# or sendgrid.SendGridBackend, or...
EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"
# if you don't already have this in settings
DEFAULT_FROM_EMAIL = "no-reply@getharper.co"



# RAVEN_CONFIG
RAVEN_CONFIG = {
    'dsn': str(os.environ.get('SENTRY_PRODUCTION_TOKEN')),
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            # To capture more than ERROR, change to WARNING, INFO, etc.
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'x'},
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry'],
        },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

# Django Filer Settings
THUMBNAIL_QUALITY = 75
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    'easy_thumbnails.processors.background',
)
THUMBNAIL_SUBDIR = 'versions'

# All Auth Config
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_EMAIL_VERIFICATION = 'none'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_NAME = 'HARPER_COOKIE'
SESSION_COOKIE_AGE = 86400
SESSION_SAVE_EVERY_REQUEST = True
ACCOUNT_SESSION_COOKIE_AGE = 86400
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# EXTRA SECURITY STUFF
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CORS_REPLACE_HTTPS_REFERER = True

# Django Celery Config
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE

# Crispy Forms Config
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Django Hijacking Settings
# Where admins are redirected to after hijacking a user
HIJACK_LOGIN_REDIRECT_URL = '/t/dashboard'
# Where admins are redirected to after releasing a user
HIJACK_LOGOUT_REDIRECT_URL = '/admin/HarperUser/user/'
HIJACK_ALLOW_GET_REQUESTS = True

# Django REST Framework Config
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10000,  # default pagination
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {  # default throttling
        'anon': '60/minute',
        'user': '100/minute'
    }
}


# Django Rest Framework JSON Web Token
JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER':
        'BaskingRidge.utils.jwt_response_payload_handler',
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=2221100),

}

# PRODUCTION / DEV SPLIT
# DEVELOPMENT ONLY
try:
    from BaskingRidge.local_settings import *

except ImportError:
    pass

# DJANGO DEBUG TOOLBAR CONFIGURATION
if DEBUG:
    MIDDLEWARE_CLASSES += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
    import debug_toolbar
    DEBUG_TOOLBAR = (
        'debug_toolbar',
    )
    INSTALLED_APPS += DEBUG_TOOLBAR

# DEBUG TOOLBAR REQUIRED IP ADDRESS
INTERNAL_IPS = '127.0.0.1'


def _smart_key(key):
    return smart_str(''.join([c for c in key if ord(c) > 32 and ord(c) != 127]))


def make_key(key, key_prefix, version):
    "Truncate all keys to 250 or less and remove control characters"
    return ':'.join([key_prefix, str(version), _smart_key(key)])[:350]

"""
WEBPACK CONFIGURATION
Decides which bundle to render in the webpack bunle finder. If Debug, then it
will default to the local bundle, but it can either by Staging or Production based
on Heroku OS Variables
"""
# Defines the webpack loader config variables
if DEBUG:
    BUNDLE_DIR_NAME = 'bundles/local/'  # end with slash
    STATS_FILE = os.path.join(BASE_DIR, 'webpack-stats-local.json')
else:
    # OPBEAT Perormace Tracking
    OPBEAT = {
        'ORGANIZATION_ID': 'b61a6b5bb31e402eafe85ddacc7826bb',
        'APP_ID': '674beb8eb3',
        'SECRET_TOKEN': '69e07cba7e99dadf47bf0069ad8d8ada71867f1c',
    }
    # If Staging - this would be set in the Heroku System Values
    if os.environ.get('STAGING'):
        BUNDLE_DIR_NAME = 'bundles/stage/'  # end with slash
        STATS_FILE = os.path.join(BASE_DIR, 'webpack-stats-stage.json')
    # Default to Production, if the os variable STAGING is not set to  True
    else:
        BUNDLE_DIR_NAME = 'bundles/prod/'  # end with slash
        STATS_FILE = os.path.join(BASE_DIR, 'webpack-stats-prod.json')

# WEBPACK LOADER
WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': BUNDLE_DIR_NAME,  # end with slash
        'STATS_FILE': STATS_FILE,
    }
}
