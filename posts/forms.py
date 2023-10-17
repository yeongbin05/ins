from django import forms
from .models import Post

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