import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sales_structure.settings')

app = Celery('sales_structure')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Планировщик стоит на 6:30 по UTC
app.conf.beat_schedule = {
    'rise-debt-every-3-hour': {
        'task': 'sale_objects.tasks.beat_debt_rise',
        'schedule': 10800
    },
    'decrease-debt-every-day-at-6-30': {
        'task': 'sale_objects.tasks.beat_debt_decrease',
        'schedule': crontab(minute='30', hour='6')
    }
}
