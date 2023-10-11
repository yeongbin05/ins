from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

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

class Post(models.Model):
    content = models.ImageField()
    text = models.CharField(max_length=300)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)