from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
urlpatterns = [
    path('',views.home,name='home'),
    path('accounts/login',auth_views.LoginView.as_view(),name='login'),
    path('',TemplateView.as_view(template_name='HOME.html'),name="home")    
]
