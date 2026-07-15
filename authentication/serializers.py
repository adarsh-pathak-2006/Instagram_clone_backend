from rest_framework.serializers import ModelSerializer, IntegerField
from authentication.models import Profile
from django.contrib.auth.models import User
class RegisterSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email', 'password']

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username']

class ProfileResourceSerializer(ModelSerializer):
    followers_count = IntegerField(source='followers.count', read_only=True)
    following_count = IntegerField(source='following.count', read_only=True)
    user=UserSerializer(read_only=True)
    class Meta:
        model=Profile
        fields=['id', 'user', 'name', 'bio', 'profile_picture', 'created_on', 'followers_count', 'following_count']

from posts.serializers import PostSerializer, ReelSerializer

class ProfileSerializer(ModelSerializer):
    user=UserSerializer(read_only=True)
    posts=PostSerializer(read_only=True, many=True)
    reels=ReelSerializer(read_only=True, many=True)
    followers_count = IntegerField(source='followers.count', read_only=True)
    following_count = IntegerField(source='following.count', read_only=True)
    class Meta:
        model=Profile
        fields=['id', 'user', 'name', 'bio', 'profile_picture', 'created_on', 'liked_posts', 'liked_reels', 'posts', 'reels', 'followers_count', 'following_count']

