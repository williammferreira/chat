from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext as _
from django.conf import settings

import uuid


# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
	theme = models.CharField(default="light", max_length=5)
	apps = models.ManyToManyField('management.App', related_name="users")

	class Meta:
		verbose_name = _("Profile")
		verbose_name_plural = _("Profiles")





@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()