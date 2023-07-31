from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path('ws/chat/<room_name>', consumers.ChatConsumer.as_asgi()),
]