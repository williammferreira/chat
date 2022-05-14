from client.extensions import *
from django.shortcuts import render
from django.views.generic import ListView, View
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ChatUser, Chats as chats
from .models import Chats

# Create your views here.


class Main(LoginRequiredMixin, ListView):
    model = chats
    template_name = "client/index.html"


class ChatsListMixin(LoginRequiredMixin, ListView):
    model = Chats
    template_name_suffix = "_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        allchats = queryset.filter(
            chatCreator=self.request.user) | queryset.filter(chatUsers__in=[self.request.user])
        ordered_queryset = allchats.order_by('-chatDateCreated')
        return ordered_queryset


class AllChatsListView(ChatsListMixin):
    pass


class RecentChatsListView(ChatsListMixin):
    def get_queryset(self):
        queryset = super().get_queryset()

        if queryset.count() > 10:
            queryset = queryset[:7]

        return queryset


class PinnedChatsListView(ChatsListMixin):
    template_name_suffix = '_list_pinned'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(pinned=True)


class InvitedChatsListView(ListView):
    model = ChatUser
    template_name_suffix = "_list_invited.html"

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            user=self.request.user, accepted=False)
        return queryset


class ChatsView(LoginRequiredMixin, View):
    def get(self, request, name, *args, **kwargs):
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
