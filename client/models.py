from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.conf import settings

import uuid

# Create your models here.


class Chat(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Creator'), on_delete=models.SET_NULL, unique=False, null=True,
                                related_name="creator")
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, verbose_name=_('Users'), through='ChatUser', unique=False, related_name="chatUser_of", blank=True)
    description = models.CharField(_('Description'), max_length=100)
    created = models.DateField(
        _('Chat Date Created'), auto_now_add=True)
    location = models.UUIDField(_('Location'), default=uuid.uuid4)
    token = models.UUIDField(_('token'), null=False, editable=False,
                             unique=True, default=uuid.uuid4)

    def get_absolute_url(self):
        return reverse_lazy("client:detail", args=[self.location])

    class Meta:
        verbose_name = _('Chat')
        verbose_name_plural = _('Chats')


class ChatUser(models.Model):
    """Intermediary model for Chat ManyToManyField."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(
        'User'), on_delete=models.CASCADE)
    chat = models.ForeignKey('Chat', verbose_name=_(
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
            return self.user.username + ' is a member of ' + self.chat.description
        else:
            return self.user.username + ' is invited to ' + self.chat.description


class Message(models.Model):
    chat = models.ForeignKey(
        Chat, on_delete=models.CASCADE, db_column="chat", related_name="messages")
    message = models.TextField()
    creator = models.TextField()
    date = models.DateTimeField()
