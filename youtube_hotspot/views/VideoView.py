from __future__ import unicode_literals

from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet
from youtube_hotspot.models.videos import Video
from youtube_hotspot.serializers.video_serializer import VideoSerializer


class VideoViewSet(MongoModelViewSet):
    """
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    """
    lookup_field = 'id'
    serializer_class = VideoSerializer

    def get_queryset(self):
        return Video.objects.all()
