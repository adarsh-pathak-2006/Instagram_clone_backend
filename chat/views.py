from django.shortcuts import render, get_object_or_404
from chat.models import Chat, Conversation
from chat.serializers import ChatSerializer, ConversationSerializer, MessageSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ChatAPI(ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=ChatSerializer

    def get_queryset(self):
        return Chat.objects.filter(user1__user=self.request.user)
    
class ConversationAPI(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, pk):
        chat_data=get_object_or_404(Chat, id=pk, user1__user=request.user)
        data=Conversation.objects.filter(chat=chat_data)
        serial=ConversationSerializer(data, many=True)
        return Response(serial.data)
    
    def post(self, request, pk):
        serial=MessageSerializer(data=request.data)
        if serial.is_valid():
            chat_data=get_object_or_404(Chat, id=pk, user1__user=request.user)
            serial.save(chat=chat_data)
            return Response({'message': 'Message sent successfully'})
        else:
            return Response(serial.errors)


    
