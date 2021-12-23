from client.extensions import *
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Chats as all_chats
from .models import Chats as chats
from .models import messages as chatMessages
from .forms import UserEditForm
from django.contrib import messages

# Create your views here.


class main(LoginRequiredMixin, ListView):
    def get(self, request, *args, **krargs):
        data = {
            'chat_number': chats.objects.filter(chatUsers__contains=request.user.username).count() + chats.objects.filter(chatCreator=request.user.username).count(),
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'username': request.user.username,
            'mychats': all_chats.objects.filter(chatCreator=request.user.username),
            'otherchats': all_chats.objects.filter(chatUsers__contains=request.user.username),
            'profile': request.user.profile,
        }
        return render(request, "client/index.html", data)


class ChatsView(LoginRequiredMixin, DetailView):
    def get(self, request, name, *args, **krargs):
        try:
            chat_name = all_chats.objects.filter(locationUrl=name, chatCreator=request.user.username).values(
                'chatDescription')[0]['chatDescription']
        except IndexError:
            try:
                chat_name = all_chats.objects.filter(locationUrl=name, chatUsers__contains=request.user.username).values(
                    'chatDescription')[0]['chatDescription']
            except:
                data = {
                    'chat_number': chats.objects.filter(chatUsers__contains=request.user.username).count() + chats.objects.filter(chatCreator=request.user.username).count(),
                    'first_name': request.user.first_name,
                    'last_name': request.user.last_name,
                    'username': request.user.username,
                    'mychats': all_chats.objects.filter(chatCreator=request.user.username),
                    'otherchats': all_chats.objects.filter(chatUsers__contains=request.user.username),
                }
                return render(request, "client/chat-not-found.html", data)
        chat_length = 0
        for i in chat_name:
            chat_length += 1
        if chat_length >= 20:
            chat_name = all_chats.objects.filter(locationUrl=name).values(
                'chatDescription')[0]['chatDescription'][0:50] + '...'
        token = chats.objects.filter(locationUrl=name).values('token')[0]['token']
        chat = chats.objects.filter(token=token)
        data = {
            'chat_number': chats.objects.filter(chatUsers__contains=request.user.username).count() + chats.objects.filter(chatCreator=request.user.username).count(),
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'username': request.user.username,
            'mychats': all_chats.objects.filter(chatCreator=request.user.username),
            'chat_name': chat_name,
            'chat_token': token,
            'otherchats': all_chats.objects.filter(chatUsers__contains=request.user.username),
            'chatMessages': chatMessages.objects.filter(chat=chat[0]),
        }
        return render(request, "client/client.html", data)


class SettingsView(LoginRequiredMixin, DetailView):
    def get(self, request):
        data = {
            'chat_number': chats.objects.filter(chatUsers__contains=request.user.username).count() + chats.objects.filter(chatCreator=request.user.username).count(),
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'username': request.user.username,
            'mychats': all_chats.objects.filter(chatCreator=request.user.username),
            'otherchats': all_chats.objects.filter(chatUsers__contains=request.user.username),
            'profile': request.user.profile,
            'auth_form': UserEditForm(instance=request.user),
        }
        return render(request, 'client/settings.html', data)
    def post(self, request):
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Account changed successfully!")
            return redirect('client:settings_view')