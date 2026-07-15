from rest_framework.serializers import ModelSerializer
from auth.serializers import ProfileResourceSerailizer
from chat.models import Chat, Conversation

class ChatSerializer(ModelSerializer):
    user1=ProfileResourceSerailizer(read_only=True)
    user2=ProfileResourceSerailizer(read_only=True)
    class Meta:
        model=Chat
        fields=['user1', 'user2', 'created']

class ConversationSerailizer(ModelSerializer):
    class Meta:
        model=Conversation
        fields='__all__'