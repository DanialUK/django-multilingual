import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Create Celery app
app = Celery('mysite')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# Configure Celery
app.conf.update(
    broker_url=os.environ.get('CELERY_BROKER_URL', 'redis://redis:6379/0'),
    result_backend=os.environ.get('CELERY_RESULT_BACKEND', 'redis://redis:6379/0'),
    accept_content=['json'],
    task_serializer='json',
    result_serializer='json',
    timezone=os.environ.get('TIME_ZONE', 'UTC'),
    task_track_started=True,
    task_time_limit=30 * 60,
    beat_scheduler='django_celery_beat.schedulers:DatabaseScheduler',
)

# Configure Celery Beat schedule
app.conf.beat_schedule = {
    'debug-task-every-30-seconds': {
        'task': 'mysite.celery.debug_task',
        'schedule': 30.0,
    },
}

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}') 