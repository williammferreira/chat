from django.dispatch import receiver
from django.db.models.signals import post_save

from client.models import Chat, ChatSettings


@receiver(post_save, sender=Chat)
def create_settings(sender, instance, created, **kwargs):
    ChatSettings.objects.create(chat=instance)
