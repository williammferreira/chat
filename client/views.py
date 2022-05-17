from client.extensions import *
from django.shortcuts import render
from django.views.generic import ListView, View
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ChatUser, Chat as chats
from .models import Chat

# Create your views here.


class Main(LoginRequiredMixin, ListView):
    model = chats
    template_name = "client/index.html"


class ChatListMixin(LoginRequiredMixin, ListView):
    model = Chat
    template_name_suffix = "_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        allchats = queryset.filter(
            creator=self.request.user) | queryset.filter(users__in=[self.request.user])
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
        queryset = super().get_queryset()
        users = ChatUser.objects.filter(
            user=self.request.user, pinned=True).values_list('chat', flat=True)
        queryset = queryset.filter(id__in=users)

        return queryset


class InvitedChatsListView(ChatListMixin):
    template_name = '_list_invited'

    def get_queryset(self):
        queryset = super().get_queryset()
        users = ChatUser.objects.filter(
            user=self.request.user, accepted=False).values_list('chat', flat=True)
        queryset = queryset.filter(id__in=users)

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
