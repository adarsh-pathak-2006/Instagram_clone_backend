from django.db import models
from authentication.models import Profile


class Chat(models.Model):
    user1=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='chat_user1')
    user2=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='chat_user2')
    created=models.DateTimeField(auto_now_add=True)

class Conversation(models.Model):
    chat=models.ForeignKey(Chat, on_delete=models.CASCADE)
    message=models.TextField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message[:100]

