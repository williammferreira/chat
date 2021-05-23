from django.urls import path, include
from client import views as client
from client.views import ChatsView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
	path('', client.main.as_view(), name="client"),
    path('chats/<str:name>', ChatsView.as_view(), name="chats_view"),
]
