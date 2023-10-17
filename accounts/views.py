from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from .forms import CustomUserChangeForm,CustomUserCreationForm
from .models import User, Follow
from posts.models import Post

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
    

def profile(request, user_name):
    User = get_user_model()
    person = User.objects.get(username=user_name)
    followers = Follow.objects.filter(follower=person)   # person을 팔로우한 follow 목록
    followings = Follow.objects.filter(following=person) # person이 팔로잉한 follow 목록
    context= {
        'person':person,
        'followers':followers,
        'followings':followings,
    }
    return render(request,'accounts/profile.html',context)


# @login_required
# def create(request,user_id):
#     print(4444)
#     if request.method == 'POST':
#         form = PostForm(request.POST,request.FILES)
#         print(request.POST)
#         print(request.FILES)
#         print(3333)
#         if form.is_valid():
#             form.save()
#             print(22222)
#         return redirect('accounts:profile', request.user)
    
#     else :
#         form = PostForm()
#         print(11111111111111111)
#     context = {
#         'form' : form,
#     }
#     return render(request,'accounts/create.html',context)


########### 팔로우 기능
@login_required
def follow(request, user_name):
    if request.method == "POST":
        person = User.objects.get(username=user_name)  # follow할 대상
        print('$$$')
        if request.user != person:
            if Follow.objects.filter(follower=person, following=request.user).exists():
                Follow.objects.filter(follower=person, following=request.user).delete()
            else:
                Follow.objects.create(follower=person, following=request.user)
            # if request.user in person.following.all():
            #     person.following.remove(request.user)
            # else:
            #     person.following.add(request.user)
        return redirect('accounts:profile', person.username)
    else:
        return HttpResponseBadRequest("Invalid Request Method")


@login_required
def unfollow(request, user_name):
    if request.method == "POST":
        person = User.objects.get(username=user_name)  # unfollow할 대상
        if Follow.objects.filter(follower=request.user, following=person).exists():
            Follow.objects.filter(follower=request.user, following=person).delete()
        return redirect('accounts:profile', person.username)
    else:
        return HttpResponseBadRequest("Invalid Request Method")
    

##########################