from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.db import database_sync_to_async
from .models import Statistic, DataItem

class DashboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        dashboard_slug = self.scope['url_route']['kwargs']['dashboard_slug']
        self.dashboard_slug = dashboard_slug
        self.room_group_name = f'stats-{dashboard_slug}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
    
    async def disconnect(self, close_code):
        print(f'Closed with code: {close_code}')
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = text_data_json['sender']

        await self.save_data_item(sender, message, self.dashboard_slug)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'statistics_message',
                'message': message,
                'sender': sender,
            }
        )

    async def statistics_message(self, event):
        message = event['message']
        sender = event['sender']

        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
        }))

    @database_sync_to_async
    def create_data_item(self, sender, message, slug):
        try:
            stat = Statistic.objects.get(slug=slug)
            data_item = DataItem.objects.create(statistic=stat, value=message, owner=sender)
            return data_item
        except Exception as e:
            print(f"Error creating DataItem: {e}")
            return None

    async def save_data_item(self, sender, message, slug):
        await self.create_data_item(sender, message, slug)