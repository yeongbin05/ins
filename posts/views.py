from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
import mimetypes
# Create your views here.
@login_required
def index(request):
    post_list = Post.objects.all()
    context = {
        'post_list':post_list,
    }
    return render(request, 'posts/index.html', context)


@login_required
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            form.save()
            return redirect('accounts:profile',request.user)
            # return redirect('posts:index')
    else:
        form = PostForm()
    context = {
        'form':form,
    }
    return render(request, 'posts/create.html', context)


@login_required
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('accounts:profile',request.user)


@login_required
def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = PostForm(instance=post)
    context = {
        'form':form,
        'post':post,
    }
    return render(request, 'posts/update.html', context)


@login_required
def likes(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user != post.user:
        if request.user in post.like_users.all():
            post.like_users.remove(request.user)
        else:
            post.like_users.add(request.user)
    return redirect('posts:index')

def comment_create(request):
    pass


# def display(request, media_id):
#     media_file = Post.objects.get(id=media_id)
    
#     mime_type, _ = mimetypes.guess_type(media_file.file.path)
    
#     if mime_type:
#         if mime_type.startswith('image'):
#             media_type = 'image'
#         elif mime_type.startswith('video'):
#             media_type = 'video'
#         else:
#             media_type = 'unknown'
#     else:
#         media_type = 'unknown'
    
#     return render(request, 'media_display.html', {'media_file': media_file, 'media_type': media_type})