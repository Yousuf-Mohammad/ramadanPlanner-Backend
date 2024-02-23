from django.conf import settings
from django.db import models

from checklist.enums import QuranReadUnit


class AbstractChecklist(models.Model):
    """
    ChecklistAbstract is an abstract model that represents a checklist.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        abstract = True
        unique_together = ("user", "date")


class QuranChecklist(AbstractChecklist):
    last_read_unit = models.CharField(
        max_length=255, choices=QuranReadUnit.choices(), blank=True
    )
    last_read_surah = models.IntegerField(blank=True)
    last_read_value = models.IntegerField(blank=True)
    completed_value = models.IntegerField(blank=True)


class SalahChecklist(AbstractChecklist):
    fardh_fajr = models.BooleanField(default=False)
    fardh_duhr = models.BooleanField(default=False)
    fardh_asr = models.BooleanField(default=False)
    fardh_maghrib = models.BooleanField(default=False)
    fardh_isha = models.BooleanField(default=False)
    sunnah_fajr = models.BooleanField(default=False)
    sunnah_duhr = models.BooleanField(default=False)
    sunnah_asr = models.BooleanField(default=False)
    sunnah_maghrib = models.BooleanField(default=False)
    sunnah_isha = models.BooleanField(default=False)
    sunnah_taraweeh = models.BooleanField(default=False)
    sunnah_tahajjud = models.BooleanField(default=False)
    sunnah_duha = models.BooleanField(default=False)


class DailyActivityChecklist(AbstractChecklist):
    pass


class DefaultChecklistItem(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ChecklistItem(models.Model):
    checklist = models.ForeignKey(
        DailyActivityChecklist, related_name="items", on_delete=models.CASCADE
    )
    default_item = models.ForeignKey(
        DefaultChecklistItem, on_delete=models.CASCADE, null=True, blank=True
    )
    custom_name = models.CharField(max_length=255, blank=True, null=True)
    is_completed = models.BooleanField(default=False)

    @property
    def name(self):
        return self.default_item.name if self.default_item else self.custom_name
