# from typing import Self
from sqlite3 import IntegrityError
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login

def home(request):
    return render(request,'Accounts/home/index.html')


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('pwd')
        role=request.POST.get('role') 
        
        try:
            User=get_user_model()
            myuser=User.objects.create_user(username, email,password)
            myuser.role=role
            myuser.save()      
            messages.success(request,"Account created succesfully")
            return redirect('home')
        
        except:
            messages.error(request,'please enter vakid credentials')
            return redirect('home')
        
    else:
        return HttpResponse('Sorry operantion cann not be performed')

def signin(request):
    if request.method=='POST':
        username = request.POST.get('loginUsername')
        password=request.POST.get('loginpwd')
        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            print("Login succesfull")
            print(user.role)
            return redirect('home')
        else:
            messages.error(request,'Bad error')
            print("Loginl")
            return redirect('home')
    else:
        print('kmkmk')



