import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rns_management_backend.settings')

app = Celery('rns_management_backend')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
