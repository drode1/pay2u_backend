from datetime import datetime
from pathlib import Path

from config.env import APPS_DIR

LOG_DIR = Path(APPS_DIR) / 'logs'

if not Path.exists(LOG_DIR):
    Path.mkdir(LOG_DIR, parents=True)

LOG_FILE_NAME = f'log-{datetime.today().strftime("%Y-%m-%d")}.log'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{name} {levelname} {asctime} {module} {process:d} {thread:d} {message}',  # noqa: E501
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': Path(LOG_DIR) / LOG_FILE_NAME,
            'when': 'W0',
            'backupCount': 10,
            'formatter': 'verbose',
            'encoding': 'utf-8',
        },
        'console': {
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': [
                'console',
                'file',
            ],
            'propagate': True,
        },
        'django.request': {
            'handlers': [
                'console',
                'file',
            ],
            'propagate': False,
        },
    },
}
