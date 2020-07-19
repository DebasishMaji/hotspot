from django.db.models import signals
from mongoengine import Document, fields, DateTimeField
import datetime


class Video(Document):
    id = fields.StringField(required=True, primary_key=True)
    title = fields.StringField(required=True)
    description = fields.StringField(required=True, null=True)
    publish_datetime = DateTimeField(default=datetime.datetime.now)
    url = fields.ListField(fields.StringField())
    updated_at = DateTimeField(default=datetime.datetime.now)
    created_at = DateTimeField(default=datetime.datetime.now)

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_at = datetime.datetime.now()


signals.pre_save.connect(Video.pre_save, sender=Video)
