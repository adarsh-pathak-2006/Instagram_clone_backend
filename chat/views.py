from django.shortcuts import render, get_object_or_404
from chat.models import Chat, Conversation
from chat.serializers import ChatSerializer, ConversationSerailizer, MessageSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response


class ChatAPI(ListCreateAPIView):
    serializer_class=ChatSerializer

    def get_queryset(self):
        return Chat.objects.filter(user1=self.request.user)
    
class ConversationAPI(APIView):
    def get(self, request, pk):
        chat_data=get_object_or_404(Chat, id=pk, user1=request.user)
        data=Conversation.objects.filter(chat=chat_data)
        serial=ConversationSerailizer(data, many=True)
        return Response(serial.data)
    
    def post(self, request, pk):
        serial=MessageSerializer(data=request.data)
        if serial.is_valid():
            chat_data=get_object_or_404(Chat, id=pk, user1=request.user)
            serial.save(chat=chat_data)
        else:
            return Response({ 'invalid':'invalid inputs' })


    
