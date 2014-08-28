""" Django settings for mm2 project.
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Application definition
THIRD_PARTY_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django.contrib.sessions',
    'django.contrib.messages',
    'rest_framework',
    'rest_framework_swagger',
]
# **************************************************************************************************
# Consider carefully the dependency graph of the app you will add to the inhouse apps list.
# Your app is able to depend on any app specified earlier in the list  and be a dependee 
# of anything specified later.
# **************************************************************************************************
INHOUSE_APPS = [
    'common',
    'hello',
    'soakinspecks',
    'analytics',
]
INSTALLED_APPS = THIRD_PARTY_APPS + INHOUSE_APPS

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'common.middleware.APIRequestMetadataMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'analytics.middleware.ContentViewMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'urls'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

USE_X_FORWARDED_HOST = True

STATIC_ROOT = '/var/www/static/'
STATIC_URL = '/static/'
MEDIA_ROOT = '/var/www/media/'
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    '/vagrant/mm2/templates/',
)

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

SWAGGER_SETTINGS = {
    'exclude_namespaces': [],  # List URL namespaces to ignore
    'api_version': '0.1',  # Specify your API's version
    'enabled_methods': [  # Specify which methods to enable in Swagger UI
        'get',
        'post',
        'put',
        'patch',
        'delete'
    ],
    'is_authenticated': True,  # Set to True to enforce user authentication,
    'is_superuser': True,  # Set to True to enforce admin only access
}

# urls without a trailing slash should not redirect
APPEND_SLASH = False
