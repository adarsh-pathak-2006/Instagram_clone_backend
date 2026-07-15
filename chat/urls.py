from django.urls import path
from chat.views import ChatAPI, ConversationAPI, StartChatAPI

urlpatterns = [
    path('chat/', ChatAPI.as_view(), name='chat'),
    path('chat/<int:pk>/', ConversationAPI.as_view(), name='conversation'),
    path('chat/start/<int:profile_pk>/', StartChatAPI.as_view(), name='start_chat'),
]
