from django.db import models


class LocationOffset(models.Model):
    """
    Settings is a model that represents the settings for the app.
    """

    country = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    offset = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
