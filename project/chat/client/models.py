from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import random

# Create your models here.

class chats(models.Model):
	chatCreator = models.TextField()
	chatUsers = models.TextField()
	chatDescription = models.TextField()
	chatDateCreated = models.TextField()
	locationUrl = models.TextField()
	token = models.TextField(primary_key=True)

	def get_absolute_url(self):
		return reverse("client:detail", args=[self.locationUrl])

	class Meta:
		db_table = 'chats'

class messages(models.Model):
	chat = models.ForeignKey(chats, on_delete=models.CASCADE)
	message = models.TextField()
	creator = models.TextField()
	date = models.DateTimeField()
	id = models.TextField(primary_key=True)
	

	class Meta:
		db_table = 'messages'

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	id = models.AutoField(primary_key=True);




@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()