from rest_framework.serializers import ModelSerializer
from authentication.models import Profile
from django.contrib.auth.models import User
from posts.serializers import PostSerializer, ReelSerializer


class RegisterSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email', 'password']

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username']

class ProfileResourceSerailizer(ModelSerializer):
    class Meta:
        model=Profile
        fields=['user', 'name', 'bio', 'created_on']

class ProfileSerializer(ModelSerializer):
    user=UserSerializer(read_only=True)
    following=ProfileResourceSerailizer(read_only=True, many=True)
    posts=PostSerializer(read_only=True, many=True)
    reels=ReelSerializer(read_only=True, many=True)
    class Meta:
        model=Profile
        fields=['user', 'name', 'bio', 'created_on', 'liked_posts', 'liked_reels', 'posts', 'reels']

