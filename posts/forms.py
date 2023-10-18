from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'cols': 100,
               
            }
        )
    )
    class Meta:
        model = Post
        fields = ['content', 'image',]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
