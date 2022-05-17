from .models import Chat


def chats(request):
    try:
        request.user.first_name
    except AttributeError:
        return {
            'chat_number': None,
            'mychats': None,
            'otherchats': None,
        }
    return {
        'chat_number': request.user.chatUser_of.count(),
        'mychats': Chat.objects.filter(creator=request.user),
        'otherchats': request.user.chatUser_of.all(),
    }


def user(request):
    try:
        request.user.first_name
    except AttributeError:
        return {
            'username': None,
            'first_name': None,
            'last_name': None,
            'profile': None,
        }
    return {
        'username': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'profile': request.user.profile,
    }
