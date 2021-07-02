import random
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from client.models import chats as all_chats
from client.models import chats
from .forms import UserChatsForm
from .dates import getdatenow
from django.utils import timezone

# Create your views here.

@login_required
def main(request):
	if request.method == "POST":
		form = UserChatsForm(request.POST)

		if form.is_valid():
			users = form.cleaned_data.get('Invites')
			name = form.cleaned_data.get('Description')
			characters = "1234567890qwertyuiopasdfghjklzxcvbnm"
			url = ""

			for i in range(0, 100):
				url = url + characters[random.randint(0,len(characters)-1)]

			token = '';
			for i in range(0, 200):
				token = token + characters[random.randint(0,len(characters)-1)]
			chat_1 = chats(
				chatCreator = f"{ request.user.username }",
				chatUsers = users,
				chatDescription = name,
				chatDateCreated = getdatenow(),
				locationUrl = url,
				token = token,
				)
			chat_1.save()
			return redirect("client")

	form = UserChatsForm()
	UserChatsForm()
	data = {
		'form': form,
		'chat_number': chats.objects.filter(chatUsers__contains = request.user.username).count() + chats.objects.filter(chatCreator = request.user.username).count(),
		'first_name': request.user.first_name,
		'last_name': request.user.last_name,
		'username': request.user.username,
		'mychats': all_chats.objects.filter(chatCreator = request.user.username),
		'otherchats': all_chats.objects.filter(chatUsers__contains = request.user.username),
	}
	return render(request, "new_chat/index.html", data)
