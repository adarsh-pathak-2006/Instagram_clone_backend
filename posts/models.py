from django.db import models
from auth.models import Profile

class Post(models.Model):
    user=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    title=models.CharField(max_length=300)
    description=models.TextField(null=True)
    attachment=models.URLField(null=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:100]
    
class Reel(models.Model):
    user=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reels')
    video=models.URLField()
    title=models.CharField(max_length=300)
    description=models.TextField(null=True)

    def __str__(self):
        return self.title[:100]
    

class PostComment(models.Model):
    user=models.ManyToManyField(Profile, related_name='comments_on_posts')
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    comment=models.TextField()

    def __str__(self):
        return self.post.title[:100]
    
class PostCommentReply(models.Model):
    user=models.ManyToManyField(Profile)
    comment=models.ForeignKey(PostComment, on_delete=models.CASCADE)
    reply=models.TextField()

    def __str__(self):
        return self.comment.comment[:100]
    
class ReelComment(models.Model):
    user=models.ManyToManyField(Profile, related_name='comments_on_reels')
    reel=models.ForeignKey(Reel, on_delete=models.CASCADE)
    comment=models.TextField()

    def __str__(self):
        return self.reel.title
    
class ReelCommentReply(models.Model):
    user=models.ManyToManyField(Profile)
    comment=models.ForeignKey(ReelComment, on_delete=models.CASCADE)
    reply=models.TextField()

    def __str__(self):
        return self.comment.comment[:100]
