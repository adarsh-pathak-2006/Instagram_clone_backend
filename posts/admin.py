from django.contrib import admin
from posts.models import Post, Reel, PostComment, ReelComment, PostCommentReply, ReelCommentReply

admin.site.register(Post)
admin.site.register(Reel)
admin.site.register(PostComment)
admin.site.register(ReelComment)
admin.site.register(PostCommentReply)
admin.site.register(ReelCommentReply)