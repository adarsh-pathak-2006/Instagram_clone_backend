from rest_framework.serializers import ModelSerializer
from authentication.serializers import ProfileResourceSerailizer
from chat.models import Chat, Conversation

class ChatSerializer(ModelSerializer):
    user1=ProfileResourceSerailizer(read_only=True)
    user2=ProfileResourceSerailizer(read_only=True)
    class Meta:
        model=Chat
        fields=['user1', 'user2', 'created']

class ConversationSerailizer(ModelSerializer):
    chat=ChatSerializer(read_only=True)
    class Meta:
        model=Conversation
        fields='__all__'

class MessageSerializer(ModelSerializer):
    class Meta:
        model=Conversation
        fields=['message']