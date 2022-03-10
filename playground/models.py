from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.hashers import make_password
from django.forms import PasswordInput
# Create your models here.
class UserProfile(models.Model):
    profile_user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_img=models.ImageField(default='images/default.png')
@receiver(post_save,sender=User)
def update_profile_signal(sender,instance,created,**kwarg):
    if created:
        UserProfile.objects.create(profile_user=instance)
    instance.userprofile.save()
class User(models.Model): 
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=30)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.CharField(max_length=30)