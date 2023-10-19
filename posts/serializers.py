from rest_framework import serializers
from .models import Post

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['image']


class PostSerializer(serializers.ModelSerializer):
   images = PostImageSerializer(many=True, read_only=True)
  
   
