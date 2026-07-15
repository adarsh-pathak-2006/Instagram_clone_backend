from django.shortcuts import get_object_or_404
from posts.models import Post, Reel, PostComment, PostCommentReply, ReelComment, ReelCommentReply
from posts.serializers import PostSerializer, ReelSerializer, PostCommentSerializer, PostCommentReplySerializer, ReelCommentSerializer, ReelCommentReplySerializer
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from authentication.models import Profile
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from authentication.throttle import InAppThrottle


class PostAPI(ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    throttle_classes=[InAppThrottle]
    serializer_class=PostSerializer

    def get_queryset(self):
        profile_data=Profile.objects.filter(user=self.request.user)
        return Post.objects.filter(user=profile_data)
    def perform_create(self, serializer):
        profile_data=Profile.objects.filter(user=self.request.user)
        serializer.save(user=profile_data)

class ReelAPI(ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    throttle_classes=[InAppThrottle]
    serializer_class=ReelSerializer

    def get_queryset(self):
        profile_data=Profile.objects.filter(user=self.request.user)
        return Reel.objects.filter(user=profile_data)
    def perform_create(self, serializer):
        profile_data=Profile.objects.filter(user=self.request.user)
        serializer.save(user=profile_data)

class PostCommentAPI(APIView):
    throttle_classes=[InAppThrottle]
    permission_classes=[IsAuthenticated]
    
    def get(self, request, pk):
        post_data=get_object_or_404(Post, id=pk)
        data=PostComment.objects.filter(post=post_data)
        serial=PostCommentSerializer(data, many=True)
        return Response(serial.data)
    
    def post(self, request, pk):
        serial=PostCommentSerializer(data=request.data)
        if serial.is_valid():
            post_data=get_object_or_404(Post, id=pk)
            user_data=get_object_or_404(Profile, user=request.user)
            comment = serial.save(post=post_data)
            comment.user.add(user_data)
            return Response({'message': 'Comment added successfully'})
        else:
            return Response(serial.errors)

class PostReplyAPI(APIView):
    throttle_classes=[InAppThrottle]
    permission_classes=[IsAuthenticated]
    def get(self, request, pk, ck):
        post_data=get_object_or_404(Post, id=pk)
        comment_data=get_object_or_404(PostComment, post=post_data, id=ck)
        reply_data=PostCommentReply.objects.filter(comment=comment_data)
        serial=PostCommentReplySerializer(reply_data, many=True)
        return Response(serial.data)
    
    def post(self, request, pk, ck):
        serial=PostCommentReplySerializer(data=request.data)
        if serial.is_valid():
            post_data=get_object_or_404(Post, id=pk)
            profile_data=get_object_or_404(Profile, user=request.user)
            comment_data=get_object_or_404(PostComment, post=post_data, id=ck)
            reply = serial.save(comment=comment_data)
            reply.user.add(profile_data)
            return Response({'message': 'Reply added successfully'})
        else:
            return Response(serial.errors)
        
class ReelCommentAPI(APIView):
    throttle_classes=[InAppThrottle]
    permission_classes=[IsAuthenticated]
    def get(self, request, pk):
        reel_data=get_object_or_404(Reel, id=pk)
        data=ReelComment.objects.filter(reel=reel_data)
        serial=ReelCommentSerializer(data, many=True)
        return Response(serial.data)
    
    def post(self, request, pk):
        serial=ReelCommentSerializer(data=request.data)
        if serial.is_valid():
            reel_data=get_object_or_404(Reel, id=pk)
            user_data=get_object_or_404(Profile, user=request.user)
            comment = serial.save(reel=reel_data)
            comment.user.add(user_data)
            return Response({'message': 'Comment added successfully'})
        else:
            return Response(serial.errors)

class ReelReplyAPI(APIView):
    throttle_classes=[InAppThrottle]
    permission_classes=[IsAuthenticated]
    def get(self, request, pk, ck):
        reel_data=get_object_or_404(Reel, id=pk)
        comment_data=get_object_or_404(ReelComment, reel=reel_data, id=ck)
        reply_data=ReelCommentReply.objects.filter(comment=comment_data)
        serial=ReelCommentReplySerializer(reply_data, many=True)
        return Response(serial.data)
    
    def post(self, request, pk, ck):
        serial=ReelCommentReplySerializer(data=request.data)
        if serial.is_valid():
            reel_data=get_object_or_404(Reel, id=pk)
            profile_data=get_object_or_404(Profile, user=request.user)
            comment_data=get_object_or_404(ReelComment, reel=reel_data, id=ck)
            reply = serial.save(comment=comment_data)
            reply.user.add(profile_data)
            return Response({'message': 'Reply added successfully'})
        else:
            return Response(serial.errors)

