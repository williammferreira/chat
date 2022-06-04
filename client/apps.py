from django.apps import AppConfig


class clientConfig(AppConfig):
    name = 'client'

    def ready(self):
        from . import signals
