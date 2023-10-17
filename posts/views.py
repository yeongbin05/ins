from django.shortcuts import render, redirect, get_object_or_404
from .models import Hashtag, Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
import re

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
            post.save()
            # 해시태그 찾아서 테이블에 넣기
            tags = re.findall(r'#[^\s#,\\]+', post.content)
            words = [tag[1:] for tag in tags]
            for word in words:
                hashtag = Hashtag.objects.get_or_create(content=word)
                post.hashtags.add(hashtag[0].pk)          
            return redirect('posts:index')
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
    return redirect('posts:index')


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



def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    hashtag_posts = hashtag.post_set.all().order_by('updated_at')
    context = {
        'hashtag': hashtag,
        'hashtag_posts' : hashtag_posts,
    }
    return render(request, 'posts/hashtag.html', context)