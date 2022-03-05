from operator import itemgetter
import MySQLdb
from django.http import HttpResponse
from tkinter.messagebox import Message
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from.models import UserProfile
from django.core.files.storage import FileSystemStorage
import mysql.connector
from django.contrib.auth.models import User
def home(request):
    return render(request,'home.html')
def user_signup(request):
    if request.method=='POST':
        user_email=request.POST['email']
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        userpass=request.POST['password']        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('signup')
        
        if User.objects.filter(email=user_email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('signup')
        user_obj = User.objects.create_user(username, user_email, userpass)
        user_obj.first_name = firstname
        user_obj.last_name = lastname

        user_obj.is_active = False
        user_obj.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        return redirect('login')
    else:
        return render(request,'signup.html')   

def user_login(request):
    con1=mysql.connector.connect(host="localhost",user="root",password="0962081628@hm",database="hena")
    cursor=con1.cursor()
    con2=mysql.connector.connect(host="localhost",user="root",password="0962081628@hm",database="hena")
    cursor2=con2.cursor()
    sqlcommand1="select username from auth_user"
    sqlcommand2="select email from auth_user"
    cursor.execute(sqlcommand1)
    cursor2.execute(sqlcommand2)
    u=[]
    e=[]
    for i in cursor:
        u.append(i)
    for j in cursor2:
        e.append(j)
    print(u)
    print(e)
    res = list(map(itemgetter(0),u))
    res1 = list(map(itemgetter(0),e))
    print(res)
    print(res1)
    k=len(res)
    i=0
    if request.method=='POST': 
        username1=request.POST.get('username')
        useremail=request.POST.get('email')
        print(username1 in res1)
        check_if_user_exists = User.objects.filter(yourtablefield="yourusername").exists()
        if username1 in res and useremail in res1 and check_if_user_exists:
                user = authenticate(username1 in res)

                messages.info(request, "Your have logged in successfully")
                return render(request,'home.html')
        else:
            messages.info(request,"check your username or password")
            return redirect('login')
    else:
        return render(request,'login.html')
#         try:
#             user=authenticate(username=username1,password=userpass1)
#             login(request,user)
#             request.session['username']=username1
#             return redirect('signup')
#         except:
#             messages.add_message(request,messages.ERROR,'can login')
#             return render(request,'login.html')
     
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






























