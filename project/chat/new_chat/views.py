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
			name = form.cleaned_data.get('Chat_Name')
			characters = "1234567890qwertyuiopasdfghjklzxcvbnm"
			url = ""

			for i in range(0, 100):
				url = url + characters[random.randint(0,len(characters)-1)]

			token = '';
			for i in range(0, 200):
				token = token + characters[random.randint(0,len(characters)-1)]
			chat_1 = chats(
				chat_creator = f"{ request.user.username }",
				chat_users = users,
				chat_name = name,
				chat_date_created = getdatenow(),
				chat_area = "",
				location_url = url,
				token = token,
				)
			chat_1.save()
			return redirect("client")

	form = UserChatsForm()
	UserChatsForm()
	data = {
		"form": form,
		'chat_number': len(all_chats.objects.all()),
		'first_name': request.user.first_name,
		'last_name': request.user.last_name,
		'username': request.user.username,
		'chats': all_chats.objects.filter(chat_creator = request.user.username),
	}
	return render(request, "new_chat/index.html", data)
