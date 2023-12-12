from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.ulogin, name="login"),
    path('register/', views.register, name="register"),
    path('logout/',views.uLogout,name='logout'),
    path('create/',views.create_tweet,name='create'),
]
