from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Account
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from home.models import Category, Post


# Create your views here.


def userSignUp(request):
    context = {}
    populer = Post.objects.all().order_by('-views')[0:10]
    Recent = Post.objects.all().order_by('-postTimeDate')[0:4]
    cat = Category.objects.all()

    
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context  = {'registration_form' : form,
                   'RecentPost': Recent,
                   'Categories': cat,
                   'Populer': populer,}
    else:  # GET request
        form = RegistrationForm()
        context  = {'registration_form' : form,
                   'RecentPost': Recent,
                   'Categories': cat,
                   'Populer': populer,}
    return render(request, 'signUp.html', context)




def userProfile(request):
    return render(request, 'user/userProfile.html')


def userLogIn(request):
    context = {}
    populer = Post.objects.all().order_by('-views')[0:10]
    Recent = Post.objects.all().order_by('-postTimeDate')[0:4]
    cat = Category.objects.all()

    if request.method == 'POST':
        em = request.POST['email']
        pas = request.POST['pass']
        user = authenticate(email=em, password=pas)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in')
            return redirect('home')
        else:
            messages.error(request, 'Not logged in')
            context  = {
                   'RecentPost': Recent,
                   'Categories': cat,
                   'Populer': populer,}
            return render(request, 'login.html', context)

    else:
        context  = {
                   'RecentPost': Recent,
                   'Categories': cat,
                   'Populer': populer,}
        return render(request, 'login.html', context)



def userLogOut(request):
    logout(request)
    messages.success(request, 'Logged out')
    return redirect('home')
