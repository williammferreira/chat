from .models import Chats

def chats(request):
    return {
        'chat_number': Chats.objects.filter(chatUsers__contains=request.user.username).count() + Chats.objects.filter(chatCreator=request.user.username).count(),
        'mychats': Chats.objects.filter(chatCreator=request.user.username),
        'otherchats': Chats.objects.filter(chatUsers__contains=request.user.username),
    }

def user(request):
    return {
        'username': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'profile': request.user.profile,
    }