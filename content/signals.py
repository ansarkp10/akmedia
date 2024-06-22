from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Content

@receiver(pre_save, sender=Content)
def update_last_updated(sender, instance, **kwargs):
    if instance.pk:  # Only update if the object already exists (not on initial save)
        instance.last_updated = timezone.now()
