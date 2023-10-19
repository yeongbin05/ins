from django import forms
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

# from .models import Post,Comment


class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("email","name","username",)
        
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = '__all__'

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('content',)
