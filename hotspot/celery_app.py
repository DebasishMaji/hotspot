import os

from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotspot.settings.development')

app = Celery('hotspot')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('hotspot.settings.celeryconfig', namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
