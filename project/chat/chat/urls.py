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
from django.contrib import admin
from django.urls import path, include
from home import views as home
from client import views as client
from client.views import ChatsView
from sign_up import views as sign_up
from new_chat import views as new_chat
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

urlpatterns = [
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("media/favicon.jpg"))),
    path('admin/', admin.site.urls),
	path('', home.main, name="home"),
	path('~', client.main.as_view(), name="client"),
	path('login/', auth_views.LoginView.as_view(template_name='login/index.html'), name='login'),
	path('signup', sign_up.main, name="sign_up"),
	path('newchat', new_chat.main, name="new_chat"),
	path('~/chats/<str:name>', ChatsView.as_view(), name="chats_view")
]
