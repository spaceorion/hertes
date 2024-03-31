
from django.contrib.auth import authenticate , login as userlogin ,logout
from .models import RegisterForm
from django.contrib.auth.forms import AuthenticationForm 
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
# Create your views here.
# def base(request):
#     if request.user.is_authenticated:
#         return render(request,'base.html')
# def index(request):
#     # if request.user.is_authenticated:
#     return render(request,'index.html')

def signup_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                ueername = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
            )
            
    else:
        form = RegisterForm()
    context = {
        "form":form
       }
        
    return render(request,'registration/signup.html',context)
def login_user(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            "form":form
        }
        return render(request,'registration/login.html',context)
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                userlogin(request,user)
                return redirect('/')
        else:
            context = {
                "form":form
            }
            return render(request,'registration/login.html',context)







