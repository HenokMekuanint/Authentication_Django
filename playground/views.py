from tkinter.messagebox import Message
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')
def signup(request):
    if request.method=="POST":
        username=request.post['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        email=request.POST['email']

        myuser=User.object.create_User(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()

        messages.success(request,"your account has been set successfully")
        return redirect('signin')
    return render(request,'signup.html')
def signin(request):
    return render(request,'signin.html')
def signout(request):
    return render(request,'signout.html')