import json
from django.utils.crypto import get_random_string
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.utils import timezone
from .models import chats, messages

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
        number = await self.numChats(text_data_json)
        await self.updateArea(text_data_json)
        rawMonth = timezone.now().strftime("%m")
        month = rawMonth.replace('01', 'January').replace('02', 'Febuary').replace('03', 'March').replace('04', 'April').replace('05', 'May').replace('06', 'June').replace('07', 'July').replace('08', 'Augest').replace('09', 'September').replace('10', 'October').replace('11', 'November').replace('12', 'December')
        now = month + ' ' + timezone.now().strftime("%d, %Y")
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
        rawMonth = timezone.now().strftime("%m")
        month = rawMonth.replace('01', 'January').replace('02', 'Febuary').replace('03', 'March').replace('04', 'April').replace('05', 'May').replace('06', 'June').replace('07', 'July').replace('08', 'Augest').replace('09', 'September').replace('10', 'October').replace('11', 'November').replace('12', 'December')
        now = month + ' ' + timezone.now().strftime("%d, %Y")

        # chats.objects.filter(token = text_data_json['token']).update(chatArea = (chats.objects.filter(token = text_data_json['token']).values('chatArea')[0]['chatArea'] + """#startdiv; class='message mymessage'#end;#startdiv; class='message-info'#end;#em;Me#emend;#break;#em;date#emend;#enddiv;#p;myMessage#endp;#enddiv;""".replace('date', now).replace('myMessage', text_data_json['message'])).encode('utf-8'))

        # chats.objects.filter(token = text_data_json['token']).update(chatArea = (f"{ chats.objects.filter(token = text_data_json['token']).values('chatArea')[0]['chatArea'] }" + '''<div class="message mymessage"><div class="message-info"><em>Me</em><br><em>date</em></div><p>myMessage</p></div>'''.replace('date', now).replace('myMessage', text_data_json['message'])).encode('utf-8'))

        # print(text_data_json['content'])
        
        # chats.objects.filter(token = text_data_json['token']).update(chatArea = text_data_json['content'] + "<div class='message mymessage'><div class='message-info'><em>Me</em><br><em>date</em></div><p>myMessage</p></div>".replace('date', now).replace('myMessage', text_data_json['message']))

        chat = chats.objects.filter(token = text_data_json['token'])[0]

        messages.objects.create(chat=chat, message=text_data_json['message'], id=get_random_string(length=1000), creator=self.user.username, date=timezone.now())

    @database_sync_to_async
    def numChats(self, text_data_json):
        chat = chats.objects.filter(token = text_data_json['token'])[0]
        return messages.objects.filter(chat=chat).count()