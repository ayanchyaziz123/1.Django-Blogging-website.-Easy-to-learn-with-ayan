from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('userSignUp/', views.userSignUp, name='userSignUp'),
    path('userLogIn/', views.userLogIn, name='userLogIn'),
    path('userLogOut/', views.userLogOut, name='userLogOut'),

]
