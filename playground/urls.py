from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView 
urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.user_signup,name='signup'),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
]
 