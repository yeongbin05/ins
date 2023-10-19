from django.urls import path
from . import views

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from . import views
# router = DefaultRouter()
# router.register('posts', views.PostViewSet)

app_name = 'posts'
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('<int:post_pk>/delete/', views.delete, name="delete"),
    path('<int:post_pk>/update/', views.update, name="update"),
    path('<int:post_pk>/likes/', views.likes, name="likes"),
    # path('display/',views.display,name='display'),
    path("<int:hash_pk>/hashtag/", views.hashtag, name="hashtag"),
    # path('i/', include(router.urls)),
]

