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