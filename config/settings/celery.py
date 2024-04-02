import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.django.base')

app = Celery('app')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(
    broker_url=os.environ.get('RMQ_BROKER_URL'),
    task_eager_propagates=True,
    task_ignore_result=True,
    task_store_errors_even_if_ignored=True,
    task_acks_late=True,
    timezone=os.environ.get('CELERY_TIME_ZONE', default='Europe/Moscow'),
    enable_utc=False,
    task_soft_time_limit=20,
    task_time_limit=30,
    task_max_retries=3,
)
