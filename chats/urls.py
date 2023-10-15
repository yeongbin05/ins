from django.urls import path
# from .views import Inbox, UserSearch, Directs, NewConversation, SendDirect
from . import views
# app_name = 'chats'
# urlpatterns = [
#    	path('', Inbox, name='inbox'),
#    	path('directs/<username>', Directs, name='directs'),
#    	path('new/', UserSearch, name='usersearch'),
#    	path('new/<username>', NewConversation, name='newconversation'),
#    	path('send/', SendDirect, name='send_direct'),

# ]
urlpatterns = [
   	path('', views.Inbox, name='inbox'),
   	path('directs/<str:username>', views.Directs, name='directs'),
   	path('new/', views.UserSearch, name='usersearch'),
   	path('new/<str:username>', views.NewConversation, name='newconversation'),
   	path('send/', views.SendDirect, name='send_direct'),

]