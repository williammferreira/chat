import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone

class ChatConsumer(AsyncWebsocketConsumer):
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
        rawMonth = timezone.now().strftime("%m")
        month = rawMonth.replace('01', 'January').replace('02', 'Febuary').replace('03', 'March').replace('04', 'April').replace('05', 'May').replace('06', 'June').replace('07', 'July').replace('08', 'Augest').replace('09', 'September').replace('10', 'October').replace('11', 'November').replace('12', 'December')
        now = month + ' ' + timezone.now().strftime("%d, %Y")
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': self.user.username,
                'datetime': now
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))
