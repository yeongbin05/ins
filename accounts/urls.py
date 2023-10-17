from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('<str:user_id>/',views.profile,name='profile'),
    # path('profile/',views.profile,name='profile'),
    path('<str:user_id>/create/',views.create,name='create'),
    path('<str:user_name>/follow', views.follow, name='follow'),
    path('<str:user_name>/unfollow', views.unfollow, name='unfollow'),
    
]
