from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, UpdateView, View

from client.extensions import *

from .models import Chat
from .models import Chat as chats
from .models import ChatUser

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
        return self.user_of


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


class ChatUserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ChatUser
    template_name = "client/chat_update.html"
    fields = ['pinned']
    success_url = reverse_lazy('client:allchats')
    success_message = _("The chat was successfully updated.")

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_object(self, queryset=None):
        queryset = self.get_queryset() if queryset is None else queryset
        chat = get_object_or_404(Chat, location=self.kwargs['location'])
        settings = get_object_or_404(queryset, chat=chat)
        return settings


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


class LeaveChatView(LoginRequiredMixin, View):
    def post(self, request):
        try:
            chat = Chat.objects.get(location=request.POST.get('location'))
            if not self.request.user == chat.creator:
                chat.users.remove(self.request.user)
                messages.success(request, _("You have left the chat."))
            return redirect('client:allchats')
        except Chat.DoesNotExist:
            return render(request, "client/chat-not-found.html")


class DeleteChatView(LoginRequiredMixin, View):
    def post(self, request):
        try:
            chat = Chat.objects.get(location=request.POST.get('location'))
            if self.request.user == chat.creator:
                chat.delete()
                messages.success(request, _("You have deleted the chat."))
            return redirect('client:allchats')
        except Chat.DoesNotExist:
            return render(request, "client/chat-not-found.html")


class TransferChatView(LoginRequiredMixin, View):
    def post(self, request):
        try:
            chat = Chat.objects.filter(location=request.POST.get('location'))
            if self.request.user == chat[0].creator:
                print(request.POST.get('users').strip())
                # chat.creator = User.objects.get(
                #     username=request.POST.get('users').strip())
                chat.update(creator=User.objects.get(
                    username=request.POST.get('users').strip()))
                # chat.creator = User.objects.get(
                # username=request.POST.get('users').strip())
                messages.success(request, _("Chat transferred successfully."))
            else:
                raise PermissionDenied()
            return redirect(reverse('client:update', args=[request.POST.get('location')]))
        except Chat.DoesNotExist:
            return render(request, "client/chat-not-found.html")


@method_decorator(csrf_exempt, name="dispatch")
class PinChatView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            chat = get_object_or_404(
                Chat, location=request.GET.get('location'))
            chatUser = get_object_or_404(
                ChatUser, chat=chat, user=self.request.user)

            if chatUser.pinned:
                chatUser.pinned = False

            else:
                chatUser.pinned = True

            chatUser.save()
            return JsonResponse({
                "success": True,
            })

        except:
            pass

        return HttpResponseNotFound()
