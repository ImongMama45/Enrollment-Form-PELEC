from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.

def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Succesfully Login")
            return redirect("login_user")
        else:
            messages.error(request,'Not valid')


    else: 
        form = RegisterForm()        
    return render(request, "accounts/register.html", {"form":form})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back user {username}')
                return redirect('dashboard')
            else: 
                messages.error(request,'Invalid username or password')
        else:
            messages.error(request,'Invalid Input')
    else: 
        form = AuthenticationForm()        
    return render(request, "accounts/login.html", {"form":form})

def logout_user(request):  
        logout(request)
        messages.info(request," You have been logged out.")
        return redirect('login_user')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')