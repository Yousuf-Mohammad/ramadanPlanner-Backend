from django.db.models.signals import post_save
from django.dispatch import receiver

from checklist.models import ChecklistItem, DailyActivityChecklist, DefaultChecklistItem


@receiver(post_save, sender=DailyActivityChecklist)
def create_default_checklist_items(sender, instance, created, **kwargs):
    if created:
        for default_item in DefaultChecklistItem.objects.all():
            ChecklistItem.objects.create(checklist=instance, default_item=default_item)
