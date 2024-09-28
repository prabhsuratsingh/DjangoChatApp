from django.urls import path, include
from ChitChat.consumer import ChatConsumer


# empty string routes to ChatConsumer, which managers chat functionality
websocket_urlpatterns = [
    path("", ChatConsumer.as_asgi()),
]
