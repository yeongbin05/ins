from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.conf import settings

def posts_image_path(instance, filename):
    
    return f'images/{instance.user.username}/{filename}'
# Create your models here.



class Hashtag(models.Model):
    content = models.CharField(max_length=200, unique=True)


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    content = models.TextField()
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    image = models.FileField(blank=True,upload_to=posts_image_path)
    # image_file = ImageSpecField(source='image', processors=[ResizeToFill(300,300)], options={'quality':90}, format="jpeg")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    content = models.CharField(max_length=200, verbose_name='댓글')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
