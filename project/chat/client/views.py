from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import chats as all_chats
from .models import chats

# Create your views here.

# @login_required
# def main(request, *args, **krargs):
# 	data = {
# 		'chat_number': all_chats.objects.all(),
# 		'first_name': request.user.first_name,
# 		'last_name': request.user.last_name,
# 		'username': request.user.username,
# 		'chats': all_chats.objects.filter(chat_creator = request.user.username),
# 	}
# 	return render(request, "main/index.html", data)

class main(LoginRequiredMixin, ListView):
	def get(self, request, *args, **krargs):
		print("test")
		data = {
			'chat_number': len(all_chats.objects.filter(chat_creator = request.user.username)),
			'first_name': request.user.first_name,
			'last_name': request.user.last_name,
			'username': request.user.username,
			'chats': all_chats.objects.filter(chat_creator = request.user.username),
		}
		print(all_chats.objects.filter(chat_creator = request.user.username).count())
		return render(request, "client/index.html", data)

class ChatsView(DetailView):
	def get(self, request, name, *args, **krargs):
		try:
			chat_name = all_chats.objects.filter(location_url = name, chat_creator = request.user.username).values('chat_name')[0]['chat_name']
		except:
			return render(request, "client/chat-not-found.html", {})
		chat_length = 0
		for i in chat_name:
			chat_length += 1
		if chat_length >= 20:
			chat_name = all_chats.objects.filter(location_url = name, chat_creator = request.user.username).values('chat_name')[0]['chat_name'][0:50] + '...'
		data = {
			'chat_number': all_chats.objects.filter(chat_creator = request.user.username).count(),
			'first_name': request.user.first_name,
			'last_name': request.user.last_name,
			'username': request.user.username,
			'chats': all_chats.objects.filter(chat_creator = request.user.username),
			'chat_name': chat_name,
			'chat_token': all_chats.objects.filter(location_url = name, chat_creator = request.user.username).values('token')[0]['token'],
		}
		return render(request, "client/client.html", data)
