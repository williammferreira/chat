from client.models import ChatUser
from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def get_chatUser_for_chat(context, chat):
    """
    Get the ChatUser object for the given chat.

    :param chat: The chat to get the ChatUser for.
    :return: The ChatUser object for the given chat.
    """

    chatUser = ChatUser.objects.get(
        chat=chat, user=context.get('request').user)

    return chatUser
