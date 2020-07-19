from django.conf import settings
from datetime import timedelta

# BROKER_URL = 'amqp://{user}:{password}@{host}:{port}//'.format(**settings.RABBITMQ_CELERY_MESSAGE_BROKER_CONFIG)
BROKER_URL = 'amqp://ssdhpcxx:rkDasoc0WOVy4gOD7FhM3jQl10zg8hjF@buck.rmq.cloudamqp.com/ssdhpcxx'

print(BROKER_URL)

CELERY_ROUTES = {
    "hotspot.tasks.stored_latest_videos": {"queue": "video"}
}


CELERYBEAT_SCHEDULE = {
    'store_latest_videos-every-1-minutes': {
        'task': 'hotspot.tasks.stored_latest_videos',
        'schedule': timedelta(seconds=30),
        'options': {
            'queue': 'video'
        }
    },
}


CELERY_TIMEZONE = 'UTC'

# All logging to be performed using celery logger
CELERY_REDIRECT_STDOUTS = False

CELERY_DISABLE_RATE_LIMITS = True

CELERY_SEND_TASK_ERROR_EMAILS = False

CELERY_ALWAYS_EAGER = False

CELERY_TASK_SERIALIZER = "json"

ADMINS = [
    ('Debasish', 'debasishmatgh92@gmail.com'),
]

