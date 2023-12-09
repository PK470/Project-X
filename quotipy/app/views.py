
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'home.html')


#register
def register(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
    
        if pass1!=pass2:
            messages.success(request,'First and second passwords are not same')
            return render(request,'register.html')
        if User.objects.filter(username=uname).exists() or User.objects.filter(email=email).exists():
            messages.success(request,'Username or email already exists')
            return render(request, 'register.html')   

        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            
                
            #print(uname,email,pass1,pass2)
            return redirect('login')  
    return render(request,'register.html')

#login
def ulogin(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        user = authenticate(request, username=uname, password=password)
        if user is not None:
            login(request, user)   
        else:
            messages.error(request, 'Please enter correct username or password')
            return render(request, 'login.html')

    return render(request, 'login.html')