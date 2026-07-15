from django.urls import path
from authentication.views import MyProfileAPI, ProfileAPI

urlpatterns = [
    path('my-profile/', MyProfileAPI.as_view(), name='profile'),
    path('path/<int:pk>/', ProfileAPI.as_view(), name='profile_individual'),
]
