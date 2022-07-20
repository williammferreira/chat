"""chat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views as client
from .views import (
    AllChatsListView,
    ChatUserUpdateView,
    ChatView,
    DeleteChatView,
    LeaveChatView,
    PinChatView,
    RecentChatsListView,
    PinnedChatsListView,
    TransferChatView,
    InvitedChatsListView,
)

app_name = "client"

urlpatterns = [
    path('', client.Main.as_view(), name="home"),
    path('chats/<str:name>', ChatView.as_view(), name="detail"),
    path('chats/', AllChatsListView.as_view(), name='allchats'),
    path("chats/recent/", RecentChatsListView.as_view(), name="recent"),
    path('chats/pinned/', PinnedChatsListView.as_view(), name="pinned"),
    path('chats/invited/', InvitedChatsListView.as_view(), name='invited'),
    path('chats/<uuid:location>/settings/',
         ChatUserUpdateView.as_view(), name='update'),
    path('chats/actions/leave/',
         LeaveChatView.as_view(), name='leave'),
    path('chats/actions/delete/',
         DeleteChatView.as_view(), name='delete'),
    path('chats/actions/transfer/',
         TransferChatView.as_view(), name='transfer'),
    path('chats/actions/pin/', PinChatView.as_view(), name='pin'),
]
