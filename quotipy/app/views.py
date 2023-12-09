
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .form import CreateUserForm

# Create your views here.
def home(request):
    return render(request, 'home.html')


#register
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                
                form.save()
                return redirect('login') 
            print('no')
        context = {'form':form }
                
        return render(request,'register.html', context)

#login
def ulogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        user = authenticate(request, username=uname, password=password)
        if user is not None:
            login(request, user)  
            return redirect('home') 
        else:
            messages.error(request, 'Please enter correct username or password')
            return render(request, 'login.html')

    return render(request, 'login.html')