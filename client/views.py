from client.extensions import *
from django.shortcuts import redirect, render
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Chats as all_chats
from .models import Chats as chats
from .models import Chats
from .models import Messages as chatMessages, Messages
from django.contrib import messages

# Create your views here.


class Main(LoginRequiredMixin, ListView):
    model = chats
    template_name = "client/index.html"


class AllChatsListView(LoginRequiredMixin, ListView):
    model = Chats
    template_name_suffix = "_list_all"

    def get_queryset(self):
        queryset = super().get_queryset()
        allchats = queryset.filter(
            chatCreator=self.request.user) | queryset.filter(chatUsers__in=[self.request.user])
        ordered_queryset = allchats.order_by('-chatDateCreated')
        return ordered_queryset


class ChatsView(LoginRequiredMixin, View):
    def get(self, request, name, *args, **krargs):
        try:
            chat = Chats.objects.get(locationUrl=name)
        except Chats.DoesNotExist:
            return render(request, "client/chat-not-found.html")

        data = {
            'chat_name': chat.chatDescription[:50] + '...',
            'chat_token': chat.token,
            'chatMessages': chat.messages.all(),
        }

        return render(request, 'client/client.html', data)
