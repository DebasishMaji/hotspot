import string

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task


# @task(name="hotspot.tasks.stored_latest_videos", ignore_result=True)
from youtube_hotspot.core.youtube_v3_data import YouTubeV3Data


@shared_task
def stored_latest_videos():
    print("started ...")
    youtube_v3_data = YouTubeV3Data()
    youtube_v3_data.get_latest_videos(3432)
