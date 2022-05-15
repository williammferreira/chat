import json
from django.utils.crypto import get_random_string
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.utils import timezone
from .models import Chats, Messages
from account.models import Profile
from .models import Chats, Messages


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.user = self.scope['user']
        self.chat = await self.get_chat(self.scope['url_route']['kwargs']['room'])
        self.room_group_name = self.user.username
        self.room_group_name = f'chat_s'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        number = await self.num_chats(text_data_json)
        raw_month = timezone.now().strftime("%m")
        month = raw_month.replace('01', 'January').replace('02', 'February').replace('03', 'March').replace('04',
                                                                                                            'April').replace(
            '05', 'May').replace('06', 'June').replace('07', 'July').replace('08', 'Augest').replace('09',
                                                                                                     'September').replace(
            '10', 'October').replace('11', 'November').replace('12', 'December')
        now = month + ' ' + timezone.now().strftime("%d, %Y, ")
        if str(timezone.now().strftime("%p")) == "AM":
            now = month + ' ' + \
                str(timezone.now().strftime("%d, %Y, %I:%M ")) + "a.m."
        else:
            now = month + ' ' + \
                str(timezone.now().strftime("%d, %Y, %I:%M ")) + "p.m."
        await self.update_area(text_data_json)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                        'creator': self.user.username,
                        'date': now,
                        'number': number,
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))

    @database_sync_to_async
    def update_area(self, text_data_json):

        chat = Chats.objects.filter(token=text_data_json['token'])[0]

        Messages.objects.create(
            chat=chat, message=text_data_json['message'], creator=self.user, date=timezone.now())

    @database_sync_to_async
    def num_chats(self, text_data_json):
        chat = Chats.objects.filter(token=text_data_json['token'])[0]
        return Messages.objects.filter(chat=chat).count()

    @database_sync_to_async
    def get_chat(self, room):
        try:
            return Chats.objects.get(token=room)
        except Chats.DoesNotExist:
            self.close(code=404)


class SearchConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.user = self.scope["user"]
        await self.accept()

    async def disconnect(self, close_code):
        await self.close()

    async def receive(self, text_data):
        search_output = await self.search(json.loads(text_data)['input'])
        await self.send(text_data=json.dumps(
            {
                        'output': search_output,
                        }
        ))

    @database_sync_to_async
    def search(self, search_terms):
        search = (list(Chats.objects.filter(creator=self.user.username,
                                            description__contains=search_terms).values_list()) + list(
            Chats.objects.filter(users__contains=self.user.username,
                                 description__contains=search_terms).values_list()))
        return search


class SettingsConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.user = self.scope["user"]
        await self.accept()

    async def disconnect(self, close_code):
        await self.close()

    async def receive(self, text_data):
        json_data = json.loads(text_data)
        await self.set_setting(json_data["setting"], json_data["value"])

    @database_sync_to_async
    def set_setting(self, setting, value):
        if setting == "theme":
            if value == "light" or value == "dark":
                Profile.objects.filter(user=self.user).update(theme=value)
