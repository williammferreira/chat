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
        settings.AUTH_USER_MODEL, verbose_name=_('Chat Users'), through='ChatUser', unique=False, related_name="chatUser_of", blank=True)
    chatDescription = models.CharField(_('Chat Description'), max_length=100)
    chatDateCreated = models.DateField(
        _('Chat Date Created'), auto_now_add=True)
    locationUrl = models.UUIDField(_('Location URL'), default=uuid.uuid4)
    token = models.UUIDField(_('token'), null=False, editable=False,
                             unique=True, default=uuid.uuid4)

    def get_absolute_url(self):
        return reverse_lazy("client:detail", args=[self.locationUrl])

    class Meta:
        verbose_name = _('Chat')
        verbose_name_plural = _('Chats')


class ChatUser(models.Model):
    """Intermediary model for Chats ManyToManyField."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(
        'User'), on_delete=models.CASCADE)
    chat = models.ForeignKey('Chats', verbose_name=_(
        'Chat'), on_delete=models.CASCADE)
    accepted = models.BooleanField(_('Accepted'), default=False)
    pinned = models.BooleanField(_('Pinned'), default=False)

    class Meta:
        """Meta definition for ChatUser."""

        verbose_name = _('ChatUser')
        verbose_name_plural = _('ChatUsers')

    def __str__(self):
        """Unicode representation of ChatUser."""
        if self.accepted:
            return self.user.username + ' is a member of ' + self.chat.chatDescription
        else:
            return self.user.username + ' is invited to ' + self.chat.chatDescription


class Messages(models.Model):
    chat = models.ForeignKey(
        Chats, on_delete=models.CASCADE, db_column="chat", related_name="messages")
    message = models.TextField()
    creator = models.TextField()
    date = models.DateTimeField()
