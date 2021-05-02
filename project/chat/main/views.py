from django.shortcuts import render
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
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
		return render(request, "main/index.html", data)

# class ChatsView(DetailView):
# 	def get(self, request, *args, **krargs):
# 		data = {
# 			"objects": all_chats.objects.filter(chat_creator = request.user.username),
# 			"chat": krargs
# 		}
# 		return render(request, "main/chat.html", data)
