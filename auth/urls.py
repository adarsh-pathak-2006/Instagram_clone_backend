from django.urls import path
from auth.views import *

urlpatterns = [
    path('profile/', ProfileAPI.as_view(), name='profile'),
]
