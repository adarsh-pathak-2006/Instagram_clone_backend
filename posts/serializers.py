from rest_framework.serializers import ModelSerializer
from authentication.serializers import ProfileResourceSerializer
from posts.models import Post, Reel, PostCommentReply, ReelCommentReply, PostComment, ReelComment


class PostSerializer(ModelSerializer):
    user=ProfileResourceSerializer(read_only=True)
    like=ProfileResourceSerializer(read_only=True, many=True)
    class Meta:
        model=Post
        fields='__all__'

class ReelSerializer(ModelSerializer):
    user=ProfileResourceSerializer(read_only=True)
    like=ProfileResourceSerializer(read_only=True, many=True)
    class Meta:
        model=Reel
        fields='__all__'

class PostCommentReplySerializer(ModelSerializer):
    user=ProfileResourceSerializer(read_only=True)
    class Meta:
        model=PostCommentReply
        fields=['user', 'reply', 'created']

class ReelCommentReplySerializer(ModelSerializer):
    user=ProfileResourceSerializer(read_only=True)
    class Meta:
        model=ReelCommentReply
        fields=['user', 'reply', 'created']

class PostCommentSerializer(ModelSerializer):
    user=ProfileResourceSerializer(read_only=True)
    replies=PostCommentReplySerializer(read_only=True, many=True)
    class Meta:
        model=PostComment
        fields=['user', 'comment', 'replies', 'created']

class ReelCommentSerializer(ModelSerializer):
    user=ProfileResourceSerializer(read_only=True)
    replies=ReelCommentReplySerializer(read_only=True, many=True)
    class Meta:
        model=ReelComment
        fields=['user', 'comment', 'replies', 'created']
