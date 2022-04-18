from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import uuid

# Create your models here.


class Chats(models.Model):
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
    chat = models.ForeignKey(Chats, on_delete=models.CASCADE, db_column="chat")
    message = models.TextField()
    creator = models.TextField()
    date = models.DateTimeField()
    id = models.TextField(primary_key=True)
    token = models.TextField()

    class Meta:
        db_table = 'messages'


class Profile(models.Model):
    DARK = 'dark'
    BLACK = 'black'
    LIGHT = 'light'
    BLUE_LINES = 'bluelines'

    THEME_CHOICES = (
        # Dark
        (DARK, 'Dark'),
        (BLACK, 'Black'),
        (BLUE_LINES, 'Blue_Lines'),

        # Light
        (LIGHT, 'Light'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, editable=False,
                          unique=True, default=uuid.uuid4)
    theme = models.CharField(choices=THEME_CHOICES,
                             default=BLACK, max_length=10)

    class Meta:
        db_table = 'profile'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
