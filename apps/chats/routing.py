from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    # url('ws/chat/room/<room_name>/', consumers.ChatConsumer),
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
    # path('ws/chat/<room_name>', consumers.ChatConsumer),
]