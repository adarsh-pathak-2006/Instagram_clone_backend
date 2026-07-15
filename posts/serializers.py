from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from posts.serializers import *
from auth.serializers import *
from posts.models import *


class PostSerializer(ModelSerializer):
    user=ProfileResourceSerailizer(read_only=True)
    class Meta:
        model=Post
        fields='__all__'

class ReelSerializer(ModelSerializer):
    user=ProfileResourceSerailizer(read_only=True)
    class Meta:
        model=Reel
        fields='__all__'

class PostCommentSerializer(ModelSerializer):
    user=ProfileResourceSerailizer(read_only=True)
    class Meta:
        model=PostComment
        fields=['user', 'comment']

class ReelCommentSerializer(ModelSerializer):
    user=ProfileResourceSerailizer(read_only=True)
    class Meta:
        model=ReelComment
        fields=['user', 'comment']

class PostCommentReplySerializer(ModelSerializer):
    user=ProfileResourceSerailizer(read_only=True)
    class Meta:
        model=PostCommentReply
        fields=['user', 'reply']

class ReelCommentReplySerializer(ModelSerializer):
    user=ProfileResourceSerailizer(read_only=True)
    class Meta:
        model=ReelCommentReply
        fields=['user', 'reply']
