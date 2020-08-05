from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

     path('', views.home, name='home'),
     path('blog/', views.blog, name='blog'),
     path('readMore/<str:slug>', views.readMore, name='post_detail'),
     path('search/', views.search, name='search'),
     path('aboutMe/', views.aboutMe, name='aboutMe'),
     path('contact/', views.contactUs, name='contact'),
     path('aboutMe/', views.aboutMe, name='aboutMe'),
     path('<slug:post>/', views.post_detail, name='readMore'),
     path('categories/<str:cat>', views.category, name='categories'),
    

]
