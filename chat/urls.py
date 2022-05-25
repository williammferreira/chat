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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from home import views as home
from new_chat import views as new_chat
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

urlpatterns = [
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("media/favicon.jpg"))),
	path('', include('home.urls', namespace="home")),
	path('~/', include('client.urls', namespace='client')),
	path('docs/', include('docs.urls', namespace='docs')),
	path('account/', include('account.urls', namespace="account")),
    path('newchat', new_chat.ChatCreateView.as_view(), name="new_chat"),
    path('apps/', include('management.urls', namespace="management")),

    path('admin/', admin.site.urls),
	path('summernote/', include('django_summernote.urls')),
    path('rosetta/', include('rosetta.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)