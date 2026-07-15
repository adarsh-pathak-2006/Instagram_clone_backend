from django.urls import path
from authentication.views import MyProfileAPI, ProfileAPI, FollowAPIView

urlpatterns = [
    path('my-profile/', MyProfileAPI.as_view(), name='profile'),
    path('path/<int:pk>/', ProfileAPI.as_view(), name='profile_individual'),
    path('follow/<int:pk>/', FollowAPIView.as_view(), name='follow'),
]
