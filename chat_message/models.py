from django.db import models


# Create your models here.
class ChatMessage(models.Model):
    sender_name = models.CharField(max_length=250)
    message_body = models.TextField()
