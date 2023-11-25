from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login1(request,):
    if request.method=='post':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login1(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login1')
    return render(request,"login1.html")
def register(request):
    return render(request, "register.html")
    if request.method=='POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if user.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif user.objects.filter(email=email).exists():
                messages.infor(request,"email already taken")
                return redirect('register')
            else:

                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
                print("user created")
        else:
            messages.info(request,"password not macthing")
            print("password not matching")
        return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')
