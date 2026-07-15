from rest_framework.serializers import ModelSerializer
from auth.models import *
from django.contrib.auth.models import User

class RegisterSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email', 'password']

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username']

class ProfileSerializer(ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Profile
        fields=['user', 'name', 'bio', 'created_on', 'liked_posts', 'liked_reels', 'posts']

class ProfileResourceSerailizer(ModelSerializer):
    class Meta:
        model=Profile
        fields=['user', 'name', 'bio', 'created_on']


