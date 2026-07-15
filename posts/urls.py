from django.urls import path
from posts.views import PostAPI, ReelAPI, PostCommentAPI, PostReplyAPI, ReelCommentAPI, ReelReplyAPI

urlpatterns = [
    path('post/', PostAPI.as_view(), name='post'),
    path('reel/', ReelAPI.as_view(), name='reel'),
    path('postcomment/<int:pk>/', PostCommentAPI.as_view(), name='post_comment'),
    path('postcomment/<int:pk>/<int:ck>/', PostReplyAPI.as_view(), name='post_comment_reply'),
    path('reelcomment/<int:pk>/', ReelCommentAPI.as_view(), name='reel_comment'),
    path('reelcomment/<int:pk>/<int:ck>/', ReelReplyAPI.as_view(), name='reel_comment_reply'),
]
