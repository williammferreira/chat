from client.extensions import *
from django.shortcuts import render
from django.views.generic import ListView, View
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ChatSettings, ChatUser, Chat, Chat as chats

# Create your views here.


class Main(LoginRequiredMixin, ListView):
    model = Chat
    template_name = "client/index.html"


class ChatListMixin(LoginRequiredMixin, ListView):
    model = Chat
    template_name_suffix = "_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.creator_of = queryset.filter(
            creator=self.request.user).order_by('-created')
        self.user_of = queryset.filter(
            users__in=[self.request.user]).order_by('-created')
        allchats = self.creator_of | self.user_of
        ordered_queryset = allchats.order_by('-created')
        return ordered_queryset


class AllChatsListView(ChatListMixin):
    pass


class RecentChatsListView(ChatListMixin):
    def get_queryset(self):
        queryset = super().get_queryset()

        if queryset.count() > 10:
            queryset = queryset[:7]

        return queryset


class PinnedChatsListView(ChatListMixin):
    template_name_suffix = '_list_pinned'

    def get_queryset(self):
        super().get_queryset()
        chats = ChatUser.objects.filter(pinned=True).values_list('chat')
        queryset = self.user_of.filter(id__in=chats)
        return queryset


class InvitedChatsListView(ChatListMixin):
    template_name_suffix = '_list_invited'

    def get_queryset(self):
        super().get_queryset()
        chats = ChatUser.objects.filter(accepted=False).values_list('chat')
        queryset = self.user_of.filter(id__in=chats)
        return queryset


class ChatView(LoginRequiredMixin, View):
    def get(self, request, name, *args, **kwargs):
        try:
            chat = Chat.objects.get(location=name)
        except Chat.DoesNotExist:
            return render(request, "client/chat-not-found.html")

        data = {
            'chat_name': chat.description[:50] + '...',
            'chat_token': chat.token,
            'chatMessages': chat.messages.all(),
        }

        return render(request, 'client/client.html', data)
