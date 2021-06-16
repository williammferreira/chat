from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
# from html import unescape
# from html.parser import HTMLParser
import html
from .models import chats as all_chats
from .models import chats, messages

# global variables

# global HTMLParse
# HTMLParse = HTMLParser.HTMLParser()

# Create your views here.

class main(LoginRequiredMixin, ListView):
	def get(self, request, *args, **krargs):
		data = {
			'chat_number': all_chats.objects.filter(chatUsers__contains = request.user.username).count(),
			'first_name': request.user.first_name,
			'last_name': request.user.last_name,
			'username': request.user.username,
			'mychats': all_chats.objects.filter(chatCreator = request.user.username),
			'otherchats': all_chats.objects.filter(chatUsers__contains = request.user.username),
		}
		return render(request, "client/index.html", data)

class ChatsView(LoginRequiredMixin, DetailView):
	def get(self, request, name, *args, **krargs):
		try:
			chat_name = all_chats.objects.filter(locationUrl = name, chatCreator = request.user.username).values('chatDescription')[0]['chatDescription']
		except IndexError:
			chat_name = all_chats.objects.filter(locationUrl = name, chatUsers__contains = request.user.username).values('chatDescription')[0]['chatDescription']
		except:
			return render(request, "client/chat-not-found.html", {})
		chat_length = 0
		for i in chat_name:
			chat_length += 1
		if chat_length >= 20:
			chat_name = all_chats.objects.filter(locationUrl = name).values('chatDescription')[0]['chatDescription'][0:50] + '...'
		token = chats.objects.filter(locationUrl = name).values('token')[0]['token']
		chat = chats.objects.filter(token=token)
		data = {
			'chat_number': chats.objects.filter(chatUsers__contains = request.user.username).count() + chats.objects.filter(chatCreator = request.user.username).count(),
			'first_name': request.user.first_name,
			'last_name': request.user.last_name,
			'username': request.user.username,
			'mychats': all_chats.objects.filter(chatCreator = request.user.username),
			'chat_name': chat_name,
			'chat_token': token,
			'otherchats': all_chats.objects.filter(chatUsers__contains = request.user.username),
			'messages': messages.objects.filter(chat=chat[0]),
		}
		return render(request, "client/client.html", data)
