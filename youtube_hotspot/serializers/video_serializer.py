from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers

from ..models.videos import Video


class VideoSerializer(mongoserializers.DocumentSerializer):
    id = serializers.CharField(read_only=False)

    class Meta:
        model = Video
        fields = '__all__'
