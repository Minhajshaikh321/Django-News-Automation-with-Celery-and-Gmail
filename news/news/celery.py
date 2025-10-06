import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','news.settings')

celery_app=Celery('news',broker='amqp://guest:guest@localhost:5672//')
celery_app.config_from_object('django.conf:settings',namespace='CELERY')
celery_app.autodiscover_tasks(['newsApp'])
