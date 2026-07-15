from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from chat.models import Chat, Conversation
from chat.serializers import ChatSerializer, ConversationSerializer, MessageSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from authentication.models import Profile


class ChatAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChatSerializer

    def get_queryset(self):
        # Return chats where the current user is EITHER user1 OR user2
        profile = get_object_or_404(Profile, user=self.request.user)
        return Chat.objects.filter(Q(user1=profile) | Q(user2=profile))

    def perform_create(self, serializer):
        profile = get_object_or_404(Profile, user=self.request.user)
        serializer.save(user1=profile)


class StartChatAPI(APIView):
    """Find or create a chat between the current user and another profile."""
    permission_classes = [IsAuthenticated]

    def post(self, request, profile_pk):
        my_profile = get_object_or_404(Profile, user=request.user)
        other_profile = get_object_or_404(Profile, id=profile_pk)

        if my_profile == other_profile:
            return Response({'error': 'You cannot chat with yourself.'}, status=400)

        # Find existing chat in either direction
        existing = Chat.objects.filter(
            Q(user1=my_profile, user2=other_profile) |
            Q(user1=other_profile, user2=my_profile)
        ).first()

        if existing:
            serial = ChatSerializer(existing)
            return Response(serial.data)

        # Create new chat
        chat = Chat.objects.create(user1=my_profile, user2=other_profile)
        serial = ChatSerializer(chat)
        return Response(serial.data, status=201)


class ConversationAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        profile = get_object_or_404(Profile, user=request.user)
        # Allow both user1 and user2 to read the conversation
        chat_data = get_object_or_404(
            Chat,
            Q(id=pk) & (Q(user1=profile) | Q(user2=profile))
        )
        data = Conversation.objects.filter(chat=chat_data).order_by('time')
        serial = ConversationSerializer(data, many=True)
        return Response(serial.data)

    def post(self, request, pk):
        profile = get_object_or_404(Profile, user=request.user)
        # Allow both participants to send messages
        chat_data = get_object_or_404(
            Chat,
            Q(id=pk) & (Q(user1=profile) | Q(user2=profile))
        )
        serial = MessageSerializer(data=request.data)
        if serial.is_valid():
            serial.save(chat=chat_data)
            return Response({'message': 'Message sent successfully'})
        else:
            return Response(serial.errors, status=400)
