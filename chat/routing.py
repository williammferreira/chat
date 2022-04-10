import django

django.setup()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import client.routing
import docs.routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            client.routing.websocket_urlpatterns
            +
            docs.routing.websocket_urlpatterns
        ),
    )
})