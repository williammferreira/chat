from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from client.models import Chats

# Create your views here.


class ChatCreateView(LoginRequiredMixin, CreateView):
    model = Chats
    template_name = 'new_chat/chats_form.html'
    fields = ['chatDescription', 'chatUsers']
    success_url = reverse_lazy("client:home")

    def form_valid(self, form):
        form.instance.chatCreator = self.request.user
        return super().form_valid(form)
