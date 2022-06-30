from django.contrib import admin

# Register your models here.
from chat_message.models import ChatMessage

admin.site.register(ChatMessage)
