"""
Django settings for qwriter_web project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os.path

# settings.configure(
#     image_proxy_key = os.environ['IMAGE_PROXY_KEY'],
#     image_link_key = os.environ['IMAGE_LINK_KEY'],
# )

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ['SECRET_KEY_DJANGO']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    SECRET_KEY = 'debugsecretkey'
    ALLOWED_HOSTS = ['*']
    LOG_HANDLERS = ['console']
    DB_HOST = 'localhost'
    DB_PASS = 'Piramida13'
    DB_USER = 'postgres'
    DB_NAME = 'postgres'
    ssl_mode = None

else:
    from dotenv import load_dotenv
    load_dotenv()
    SECRET_KEY = os.environ['SECRET_KEY_DJANGO']
    ALLOWED_HOSTS = ['awse.us', 'www.awse.us']
    LOG_HANDLERS = ['console']
    SECURE_SSL_REDIRECT = False
    PREPEND_WWW = True
    DB_HOST = 'ec2-174-129-225-160.compute-1.amazonaws.com'
    DB_USER = 'fqyqcmmltfyacx'
    DB_NAME = 'dbmhdf1ft2d1ga'
    DB_PASS = os.environ['DB_PASS']
    ssl_mode = 'require'


NEWSAPI_TOKEN = os.environ['NEWS_API_TOKEN'].split()

RETOKEN_PUBLIC = os.environ['RECAPTCHA_PUBLIC_KEY']
RETOKEN_PRIVATE = os.environ['RECAPTCHA_PRIVATE_KEY']

IMAGE_PROXY_KEY = os.environ['IMAGE_PROXY_KEY']
IMAGE_PROXY_LINK_KEY = os.environ['IMAGE_LINK_KEY']
LOAD_MORE_ENCRYPT_KEY = os.environ['LOAD_MORE_KEY']
SIGN_ENCRYPT_KEY = os.environ['SIGN_ENCRYPT_KEY']

SEARCH_CX = os.environ['SEARCH_CX']
SEARCH_API_HOST = os.environ['SEARCH_API_HOST']
SEARCH_API_KEYS = os.environ['SEARCH_API_KEYS']
BOT_CHECK_TOKEN = os.environ['BOT_CHECK_TOKEN']

TIKTOK_PAGE_ENABLED = False

# Application definition

INSTALLED_APPS = [
    'my_web',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'compressor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'my_web.middleware.Compressor_AWARE',
]

ROOT_URLCONF = 'qwriter_web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'qwriter_web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': DB_HOST,
        'PORT': '5432',
        'OPTIONS': {'sslmode': ssl_mode},
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': LOG_HANDLERS,
            'propagate': True,
        },
    }
}

STATICFILES_FINDERS = (
   'django.contrib.staticfiles.finders.FileSystemFinder',
   'django.contrib.staticfiles.finders.AppDirectoriesFinder',
   'compressor.finders.CompressorFinder',
)

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
#STATICFILES_DIRS = (
#    # os.path.join(BASE_DIR, '../my_web/static'),
#    '/home/code/qwriter_web/my_web/static',
#)

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# 22.04.2021
