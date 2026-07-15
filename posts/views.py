from django.shortcuts import render, get_object_or_404
from posts.models import Post, Reel, PostComment, PostCommentReply, ReelComment, ReelCommentReply
from posts.serializers import PostSerializer, ReelSerializer, PostCommentSerializer, PostCommentReplySerializer, ReelCommentSerializer, ReelCommentReplySerializer
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from auth.models import Profile
from rest_framework.response import Response


class PostAPI(ListCreateAPIView):
    serializer_class=PostSerializer

    def get_queryset(self):
        profile_data=Profile.objects.filter(user=self.request.user)
        return Post.objects.filter(user=profile_data)
    def perform_create(self, serializer):
        profile_data=Profile.objects.filter(user=self.request.user)
        serializer.save(user=profile_data)

class ReelAPI(ListCreateAPIView):
    serializer_class=ReelSerializer

    def get_queryset(self):
        profile_data=Profile.objects.filter(user=self.request.user)
        return Reel.objects.filter(user=profile_data)
    def perform_create(self, serializer):
        profile_data=Profile.objects.filter(user=self.request.user)
        serializer.save(user=profile_data)

class PostCommentAPI(APIView):
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
            serial.save(post=post_data, user=user_data)
        else:
            return Response({ 'invalid':'invalid inputs' })

class PostReplyAPI(APIView):
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
            serial.save(user=profile_data, comment=comment_data)
        else:
            return Response({ 'invalid':'invalid inputs' })
        
class ReelCommentAPI(APIView):
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
            serial.save(reel=reel_data, user=user_data)
        else:
            return Response({ 'invalid':'invalid inputs' })

class ReelReplyAPI(APIView):
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
            serial.save(user=profile_data, comment=comment_data)
        else:
            return Response({ 'invalid':'invalid inputs' })

