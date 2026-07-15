from rest_framework.serializers import ModelSerializer
from authentication.serializers import ProfileResourceSerializer
from chat.models import Chat, Conversation

class ChatSerializer(ModelSerializer):
    user1=ProfileResourceSerializer(read_only=True)
    user2=ProfileResourceSerializer(read_only=True)
    class Meta:
        model=Chat
        fields=['user1', 'user2', 'created']

class ConversationSerializer(ModelSerializer):
    chat=ChatSerializer(read_only=True)
    class Meta:
        model=Conversation
        fields='__all__'

class MessageSerializer(ModelSerializer):
    class Meta:
        model=Conversation
        fields=['message']