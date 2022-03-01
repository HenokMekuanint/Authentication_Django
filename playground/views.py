from tkinter.messagebox import Message
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.
def index(request):
    return render(request,'index.html')
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        email=request.POST['email']

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()

        messages.success(request,"your account has been set successfully")
        return redirect('signin')
    return render(request,'signup.html')
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            return redirect(request,"index.html",{"fname":fname})
        else:
            messages.error(request,"bad credentails")
            redirect(request,"home")
    return render(request,'signin.html')
def signout(request):
    return render(request,'signout.html')