from django.db import models

from content.enums import ContentType


class Content(models.Model):
    """
    Content is a model that represents a piece of content.
    """

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=255, choices=ContentType.choices())
    image = models.ImageField(upload_to="images", blank=True)
    active_start = models.DateTimeField(blank=True, null=True)
    active_end = models.DateTimeField(blank=True, null=True)
