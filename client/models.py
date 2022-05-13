from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.conf import settings

import uuid

# Create your models here.


class Chats(models.Model):
    chatCreator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Chat Creator'), on_delete=models.SET_NULL, unique=False, null=True,
                                    related_name="chatCreator")
    chatUsers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, verbose_name=_('Chat Users'),  unique=False, related_name="chatUser_of", blank=True)
    chatDescription = models.CharField(_('Chat Description'), max_length=100)
    chatDateCreated = models.DateField(
        _('Chat Date Created'), auto_now_add=True)
    locationUrl = models.UUIDField(_('Location URL'), default=uuid.uuid4)
    token = models.UUIDField(_('token'), null=False, editable=False,
                             unique=True, default=uuid.uuid4)
    pinned = models.BooleanField(_('Pinned'), default=False)

    def get_absolute_url(self):
        return reverse_lazy("client:detail", args=[self.locationUrl])

    class Meta:
        verbose_name = _('Chat')
        verbose_name_plural = _('Chats')


class Messages(models.Model):
    chat = models.ForeignKey(
        Chats, on_delete=models.CASCADE, db_column="chat", related_name="messages")
    message = models.TextField()
    creator = models.TextField()
    date = models.DateTimeField()
