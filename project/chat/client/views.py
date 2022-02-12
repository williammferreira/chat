from re import template
from client.extensions import *
from django.shortcuts import redirect, render
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Chats as all_chats
from .models import Chats as chats
from .models import messages as chatMessages
from django.contrib import messages

# Create your views here.


class Main(LoginRequiredMixin, ListView):
    model = chats
    template_name = "client/index.html"


class ChatsView(LoginRequiredMixin, View):
    def get(self, request, name, *args, **krargs):
        try:
            chat_name = all_chats.objects.filter(locationUrl=name, chatCreator=request.user.username).values(
                'chatDescription')[0]['chatDescription']
        except IndexError:
            try:
                chat_name = all_chats.objects.filter(locationUrl=name, chatUsers__contains=request.user.username).values(
                    'chatDescription')[0]['chatDescription']
            except:
                return render(request, "client/chat-not-found.html")
        chat_length = 0
        for i in chat_name:
            chat_length += 1
        if chat_length >= 20:
            chat_name = all_chats.objects.filter(locationUrl=name).values(
                'chatDescription')[0]['chatDescription'][0:50] + '...'
        token = chats.objects.filter(locationUrl=name).values('token')[0]['token']
        chat = chats.objects.filter(token=token)
        data = {
            'chat_name': chat_name,
            'chat_token': token,
            'chatMessages': chatMessages.objects.filter(chat=chat[0]),
        }
        return render(request, "client/client.html", data)