import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import Group, User

class ChatRoomConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['chat_box_name']
        self.room_group_name = 'chat_%s' % self.room_name
        
        # username = str(self.scope["user"])
        # user = User.objects.filter(username = username).first()
        # if str(Group.obejcts.filter(user = user).first()) == "Patient":
        #     self.patient_is_connected = True
        # elif str(Group.obejcts.filter(user = user).first()) == "Staff":
        #     self.staff_is_connected = True
        # print(self.patient_is_connected)
        # print(self.staff_is_connected)

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        
        # username = str(self.scope["user"])
        # user = User.objects.filter(username = username).first()
        # if str(Group.obejcts.filter(user = user).first()) == "Patient":
        #     self.patient_is_connected = False
        # elif str(Group.obejcts.filter(user = user).first()) == "Staff":
        #     self.staff_is_connected = False
        # print(self.patient_is_connected)
        # print(self.staff_is_connected)
        
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']
        group = text_data_json['group']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message,
                'username': username,
                'group': group
            }
        )

    async def chatroom_message(self, event):
        message = event['message']
        username = event['username']
        group = event['group']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'group': group
        }))

    pass
