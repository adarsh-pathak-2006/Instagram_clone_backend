from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=120)
    bio=models.TextField(null=True)
    created_on=models.DateTimeField(auto_now_add=True)
    post_liked=models.ManyToManyField("posts.Post", related_name='profile_post_liked', null=True)
    reel_liked=models.ManyToManyField("posts.Reel", related_name='profile_reel_liked', null=True)
    
    def __str__(self):
        return self.user.username


#serializers abhi shi krna hai dhyam rkhna