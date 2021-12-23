import json
from django.utils.crypto import get_random_string
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.utils import timezone
from .models import Chats, messages, Profile

class ChatConsumer(AsyncWebsocketConsumer):
    channel_layer_alias = "chatConsumer"

    async def connect(self):
        self.user = self.scope['user']
        # self.id = self.scope['url_route']['kwargs']['room']
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
        number = await self.numChats(text_data_json)
        rawMonth = timezone.now().strftime("%m")
        month = rawMonth.replace('01', 'January').replace('02', 'Febuary').replace('03', 'March').replace('04', 'April').replace('05', 'May').replace('06', 'June').replace('07', 'July').replace('08', 'Augest').replace('09', 'September').replace('10', 'October').replace('11', 'November').replace('12', 'December')
        now = month + ' ' + timezone.now().strftime("%d, %Y, ")
        if (str(timezone.now().strftime("%p")) == "AM"):
            now = month + ' ' + str(timezone.now().strftime("%d, %Y, %I:%M ")) + "a.m."
        else:
            now = month + ' ' + str(timezone.now().strftime("%d, %Y, %I:%M ")) + "p.m."
        await self.updateArea(text_data_json)
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
    def updateArea(self, text_data_json):

        chat = chats.objects.filter(token = text_data_json['token'])[0]

        messages.objects.create(chat=chat, message=text_data_json['message'], id=get_random_string(length=1000), creator=self.user.username, date=timezone.now(), token = chat.token)

    @database_sync_to_async
    def numChats(self, text_data_json):
        chat = chats.objects.filter(token = text_data_json['token'])[0]
        return messages.objects.filter(chat=chat).count()

class SearchConsumer(AsyncWebsocketConsumer):
    channel_layer_alias = "searchConsumer"

    async def connect(self):
        self.user = self.scope["user"]
        await self.accept()

    async def disconnect(self, close_code):
        await self.close();

    async def receive(self, text_data):
        searchOutput = await self.search(json.loads(text_data)['input'])
        await self.send(text_data=json.dumps(
            {
                'output': searchOutput,
            }
        ))

    @database_sync_to_async
    def search(self, searchTerms):
        search = (list(chats.objects.filter(chatCreator = self.user.username, chatDescription__contains = searchTerms).values_list()) + list(chats.objects.filter(chatUsers__contains = self.user.username, chatDescription__contains = searchTerms).values_list()))
        return search

class SettingsConsumer(AsyncWebsocketConsumer):
    channel_layer_alias = "settingsConsumer"

    async def connect(self):
        self.user = self.scope["user"]
        await self.accept()

    async def disconnect(self, close_code):
        await self.close();

    async def receive(self, text_data):
        json_data = json.loads(text_data)
        await self.setSetting(json_data["setting"], json_data["value"])
    
    @database_sync_to_async
    def setSetting(self, setting, value):
        if setting == "theme":
            if value == "light" or value == "dark":
                Profile.objects.filter(user=self.user).update(theme=value)