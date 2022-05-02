from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.utils.translation import gettext_lazy as _
import uuid


# Create your models here.


class Profile(models.Model):
    DARK = 'dark'

    LIGHT = 'light'

    THEME_CHOICES = (
        # Dark Theme
        (DARK, 'Dark'),

        # Light Theme
        (LIGHT, 'Light'),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, verbose_name=_('User'), on_delete=models.CASCADE)
    theme = models.CharField(
        _('Theme'), choices=THEME_CHOICES, default="black", max_length=10)
    apps = models.ManyToManyField('management.App', related_name="users")

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()
