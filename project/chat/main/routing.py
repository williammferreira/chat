from django.urls import path
from . import consumers
websocket_urlpatterns = [
    path(r'ws/chat/room/<room>', consumers.ChatConsumer.as_asgi())
]
