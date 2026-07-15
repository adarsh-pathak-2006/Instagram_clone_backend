from rest_framework.serializers import ModelSerializer
from auth.serializers import ProfileResourceSerailizer
from posts.models import Post, Reel, PostCommentReply, ReelCommentReply, PostComment, ReelComment


class PostSerializer(ModelSerializer):
    user=ProfileResourceSerailizer(read_only=True)
    like=ProfileResourceSerailizer(read_only=True, many=True)
    class Meta:
        model=Post
        fields='__all__'

class ReelSerializer(ModelSerializer):
    user=ProfileResourceSerailizer(read_only=True)
    like=ProfileResourceSerailizer(read_only=True, many=True)
    class Meta:
        model=Reel
        fields='__all__'

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

class PostCommentSerializer(ModelSerializer):
    user=ProfileResourceSerailizer(read_only=True)
    replies=PostCommentReplySerializer(read_only=True)
    class Meta:
        model=PostComment
        fields=['user', 'comment', 'replies']

class ReelCommentSerializer(ModelSerializer):
    user=ProfileResourceSerailizer(read_only=True)
    replies=ReelCommentReplySerializer(read_only=True)
    class Meta:
        model=ReelComment
        fields=['user', 'comment']
