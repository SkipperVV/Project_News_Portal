import os
from celery import Celery
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'News_Portal.settings')
 
app = Celery('News_Portal')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'print_every_5_seconds': {
        'task': 'Models.tasks.hello',
        'schedule': 5,
    },
}