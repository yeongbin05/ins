from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm,CustomUserCreationForm,PostForm
from .models import Post
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


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('accounts:index')
    
def profile(request,user_id):
    posts = Post.objects.all()
    context= {
        'posts' : posts,
    }
    return render(request,'accounts/profile.html',context)

def create(request):
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