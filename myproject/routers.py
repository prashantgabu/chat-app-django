from rest_framework import routers

from chat_message.views import ChatMessageViewSet

router = routers.DefaultRouter()

router.register(r'chat_message', ChatMessageViewSet)
