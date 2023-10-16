from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
# 수정부분 이미지 저장경로설정
def articles_image_path(instance, filename):
    
    return f'images/{instance.user.username}/{filename}'

from django.contrib.auth.models import AbstractUser
from django.conf import settings
class User(AbstractUser):
    name = models.CharField(max_length=100)
    # password = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    # email = models.CharField(max_length=100)
    birthday = models.DateField(null=True)
    bluebadge = models.BooleanField(default=False)
    profileimage = models.ImageField(null=True)
    # is_active = models.BooleanField(null=True)
    following = models.ManyToManyField('self', through='Follow', symmetrical=False, blank=True)


class Post(models.Model):
    # content = models.ImageField()
    content = models.ImageField(upload_to=articles_image_path)
    text = models.CharField(max_length=300)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)



class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='follow_me', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='i_follow', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')
    


