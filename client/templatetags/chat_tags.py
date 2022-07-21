from client.models import ChatUser
from django.contrib.auth import get_user_model
from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def get_chatUser_for_chat(context, chat, user=None):
    """
    Get the ChatUser object for the given chat.

    :param chat: The chat to get the ChatUser for.
    :param user: The user for the ChatUser.
    :return: The ChatUser object for the given chat and user.
    """

    if user:
        chatUser = ChatUser.objects.get(
            chat=chat, user=get_user_model().objects.get(id=user))
    else:
        chatUser = ChatUser.objects.get(
            chat=chat, user=context.get('request').user)

    return chatUser
