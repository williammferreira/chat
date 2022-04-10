from django.urls import path
from .consumers import DocsConsumer


websocket_urlpatterns = [
    path(r'ws/docs/DocsConsumer', DocsConsumer.as_asgi()),
]