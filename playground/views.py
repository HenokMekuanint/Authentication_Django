from django.http import HttpResponse
from tkinter.messagebox import Message
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from playground.form import loginform
from.models import UserProfile
from django.core.files.storage import FileSystemStorage
  
def home(request):
    return render(request,'home.html')
def user_signup(request):
    if request.methon=='POST':
        user_email=request.POST['email']
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        userpass=request.POST['password']
        try:
            user_obj=User.objects.create(username=username,email=user_email,fname=firstname,lame=lastname)
            user_obj.set_password(userpass)
            user_obj.save()
            user_auth=authenticate(username=username,password=userpass)
            login(request,user_auth)
            return redirect('home')
        except:
            messages.add_message(request,messages.ERROR,'can not sign up')
            return render(request,'user_profile/signup.html')
    return render(request,'signup.html')
def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        userpass=request.POST['password']
        try:
            user_obj=authenticate(username=username,password=userpass)
            login(request,user_obj)
            request.session['username']=username
            return redirect('home')
        except:
            messages.add_message(request,messages.ERROR,'can login')
            return render(request,'login.html')
    else:
        return render(request,'login.html')
def user_logout(request):
    try:
        logout(request)
    except:

        return redirect('home')
@login_required
def user_profile(request,user_id):
    if request.method=='POST':
        user_obj=User.objects.get(id=user_id)
        user_profile_obj=user_profile.objects.get(id=user_id)
        user_img=request.Files['user_img']
        fs_handle=FileSystemStorage()
        img_name='images/user_{0}'.format(user_id)
        if fs_handle.exists(img_name):
            fs_handle.delete(img_name)
        fs_handle.save(img_name,user_img)
        user_profile_obj.profile_img=img_name
        user_profile_obj.save()
        user_profile_obj.refresh_from_db()
        return render(request,'my_profile.html',{'my_profile':user_profile_obj})   
    if(request.user.is_authenticated and request.user.id==user_id):
        user_obj=User.objects.get(id=user_id)
        user_profile=UserProfile.objects.get(id=user_id)
        return render(request,'my_profile.html',{'my_profile':user_profile})






























