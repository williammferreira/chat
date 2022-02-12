"""
ASGI config for chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.urls import re_path

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat.settings')
# django_asgi_app = get_asgi_application()

# import client.routing
# from client import consumers
# from channels.auth import AuthMiddlewareStack

# application = ProtocolTypeRouter({
#     'websocket': AuthMiddlewareStack(
#         URLRouter(
#                 client.routing.websocket_urlpatterns
#         )
#     ),
# })

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
# # Initialize Django ASGI application early to ensure the AppRegistry
# # is populated before importing code that may import ORM models.
# django_asgi_app = get_asgi_application()

# from client.routing import websocket_urlpatterns
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.conf.urls import url

# application = ProtocolTypeRouter({
#     # Django's ASGI application to handle traditional HTTP requests
#     "http": django_asgi_app,

#     # WebSocket chat handler
#     "websocket": AuthMiddlewareStack(
#         URLRouter(websocket_urlpatterns)
#     ),
# })

"""
ASGI config for chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat.settings.local')

application = get_asgi_application()