""" Settings specific to development environments
"""

from settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase.sqlite3',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)-8s %(asctime)s %(module)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)-8s %(asctime)s %(message)s'
        },
    },
    'filters': {
    'debug': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'log_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/vagrant/demo/logs/demo.log',
            'maxBytes': 500000,
            'backupCount': 0,
            'formatter': 'verbose',
        },
        'request_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/vagrant/demo/logs/request.log',
            'maxBytes': 500000,
            'backupCount': 0,
            'formatter': 'verbose',
        },
        'db_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/vagrant/demo/logs/db.log',
            'maxBytes': 500000,
            'backupCount': 0,
            'formatter': 'simple',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['log_file', ],
            'propagate': True,
            'level': 'WARN',
        },
        'django.request': {
            'handlers': ['request_file', ],
            'level': 'INFO',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['db_file', ],
            'level': 'DEBUG',
            'propagate': False,
        },
        '': {
            'handlers': ['log_file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#r#zxgm^8hw=q28co*-x3^@her!i9&6p$cb4ifvda_buobz$tg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

#### DON'T PUT ANYTHING BELOW THIS!!!!!
try:
    from settings.local import *
except ImportError:
    pass
#### TYPE BELOW THIS AND VOID YOUR WARRANTY!!!
