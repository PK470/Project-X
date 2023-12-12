from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .form import CreateUserForm, TweetForm
from .models import *
from django.contrib.auth.decorators import login_required


#Create your views here.
def home(request):
    tweet = Tweet.objects.all()
    context = {'context': tweet}
    return render(request, 'home.html', context)


#register
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()  # Save the user
                new_profile = Profile.objects.create(user= user)  
                new_profile.add_self_to_follows()
                
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
def uLogout(request):
    logout(request)
    return redirect('login')
@login_required
def create_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
           
            tweet = form.save(commit=False)
            tweet.user_profile = request.user.profile  
            tweet.save()

            return redirect('home')
    else:
        form = TweetForm()

    return render(request, 'create_tweet.html', {'form': form})