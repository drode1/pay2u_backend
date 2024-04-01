import os

from celery import Celery
from django.conf import settings

CELERY_BROKER_URL = os.environ.get('RMQ_BROKER_URL')
CELERY_RESULT_BACKEND = 'django-db'

CELERY_TIMEZONE = 'UTC'

CELERY_TASK_SOFT_TIME_LIMIT = 20  # seconds
CELERY_TASK_TIME_LIMIT = 30  # seconds
CELERY_TASK_MAX_RETRIES = 3

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.django.base')

app = Celery('my_app')
# celery -A my_app.tasks worker

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
