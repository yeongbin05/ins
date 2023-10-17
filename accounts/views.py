from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from .forms import CustomUserChangeForm,CustomUserCreationForm,PostForm,CommentForm
from .models import User, Post, Follow,Comment
# Create your views here.
def index(request):
    posts = Post.objects.all()
    form = AuthenticationForm()
    context= {
        'posts' : posts,
        'form' : form,
    }
    return render(request,'accounts/index.html',context)

def signup(request):
    if request.method == 'POST':
        print(1)
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            
            user=form.save()
            auth_login(request,user)
            
            
            return redirect('accounts:index')
        
    else :
        form = CustomUserCreationForm()

    context = {
        'form' : form,
    }
    return render(request,'accounts/signup.html',context)


def login(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect(request.GET.get('next') or 'accounts:index')
        
    else : 
        form = AuthenticationForm()
    context = {
        'form' : form,
    }

    return render(request,'accounts/login.html',context)


@login_required
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('accounts:index')
    

def profile(request, user_id):
    
    user = User.objects.get(username=user_id)  # follow할 대상

    followers = Follow.objects.filter(follower=user)
    followings = Follow.objects.filter(following=user)
    
    posts = Post.objects.all()
    
    profile = User.objects.get(username=user_id)
    context= {
        'posts' : posts,
        'profile':profile,
        'followers' : followers,
        'followings' : followings,
        'comment_form' : CommentForm,
    }
    return render(request,'accounts/profile.html',context)


@login_required
def create(request,user_id):
    print(4444)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        print(request.POST)
        print(request.FILES)
        print(3333)
        if form.is_valid():
            form.save()
            print(22222)
        return redirect('accounts:profile', request.user)
    
    else :
        form = PostForm()
        print(11111111111111111)
    context = {
        'form' : form,
    }
    return render(request,'accounts/create.html',context)


########### 팔로우 기능
@login_required
def follow(request, user_name):
    if request.method == "POST":
        user_to_follow = User.objects.get(username=user_name)  # follow할 대상
        print('$$$')
        if request.user != user_to_follow:
            if request.user in user_to_follow.following.all():
                user_to_follow.following.remove(request.user)
            else:
                user_to_follow.following.add(request.user)
            # if Follow.objects.filter(follower=request.user, following=user_to_follow).exists():
            #     Follow.objects.filter(follower=request.user, following=user_to_follow).delete()
            # else:
            #     Follow.objects.create(follower=request.user, following=user_to_follow)
        return redirect('accounts:profile', user_to_follow.username)
    else:
        return HttpResponseBadRequest("Invalid Request Method")


@login_required
def unfollow(request, user_name):
    if request.method == "POST":
        user_to_unfollow = User.objects.get(username=user_name)  # unfollow할 대상
        if Follow.objects.filter(follower=request.user, following=user_to_unfollow).exists():
            Follow.objects.filter(follower=request.user, following=user_to_unfollow).delete()
        return redirect('accounts:profile', user_to_unfollow.username)
    else:
        return HttpResponseBadRequest("Invalid Request Method")
    

##########################

def test(request,user_name):
            
    user = User.objects.get(username=user_name)  # follow할 대상

    followers = Follow.objects.filter(follower=user)
    context = {
        'followers' : followers,
    }
    return render(request,'accounts/test.html', context)


# def comments_create(request,pk):
#     post = Post.objects.get(pk=pk)
#     comment_form = CommentForm(request.POST)
#     if comment_form.is_valid():
#         comment = comment_form.save(commit=False)
#         comment.post = post
#         comment_form.save()
#         return redirect('accounts:profile',post.pk)
    
#     context = {
#         'post' : post,
#         'comment_form' : comment_form,
#     }
#     return render(request,'accounts/profile.html',context)