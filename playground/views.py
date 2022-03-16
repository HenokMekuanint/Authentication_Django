import email
from operator import itemgetter
from telnetlib import ENCRYPT
import MySQLdb
from django.http import HttpResponse
from tkinter.messagebox import Message
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from mysqlx import Auth
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
        password=request.POST['password']        
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
        user_obj = User.objects.create_user(username, user_email)
        user_obj.first_name = firstname
        user_obj.last_name = lastname
        user_obj.password=password

        user_obj.is_active = False
        user_obj.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        return redirect('login')
    else:
        return render(request,'signup.html')   

def user_login(request):
    con1=mysql.connector.connect(host="localhost",user="root",password="0962081628@hm",database="hena")
    cursor=con1.cursor()
    sqlcommand1="select username from auth_user"


    cursor.execute(sqlcommand1)
    u=[]
    
    print(cursor)
    for i in cursor:
        u.append(i)
    res = list(map(itemgetter(0),u))
    if request.method=='POST':
        username=request.POST.get('username')
        userpass=request.POST.get('password')
        check_if_user_exists = User.objects.filter(username=username).exists()

        if username in res and check_if_user_exists :
                User.is_authenticated=True

                con3=mysql.connector.connect(host="localhost",user="root",password="0962081628@hm",database="hena")
                cursor3=con3.cursor()
                sqlcommand3="select password from auth_user where username=%s"
                cursor3.execute(sqlcommand3, (username,))
                n=[]
                for i in cursor3:
                    n.append(i)
                res3=list(map(itemgetter(0),n))
                print(res3)

                if res3[0]==userpass:
                    messages.info(request, "Your have logged in successfully")
                    messages.info(request,"hi  "+username)
                    return render(request,'home.html',)
                else:
                    messages.info(request,"you have enterd incorrect password")
                    return redirect('login')
        else:
            messages.info(request,"incorrect username")
            return redirect('login')
    else:
        return render(request,'login.html')
     
def user_logout(request):
    try:
        logout(request)
    except:

        return redirect('home')































