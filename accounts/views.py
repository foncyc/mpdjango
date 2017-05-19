# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            message = "Successfully Logged In"
            # return render(request, 'beta/beta.html', {'message':message})
            return redirect('beta_home')
        else:
            message = "Error Signing in"
            return render(request, 'accounts/login.html', {'message':message})
    else: 
        return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    message = "Successfully Logged Out"
    return render(request, 'beta/beta.html', {'message':message})

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            message = "Account exists. Choose another user or try logging in."
            return render(request, 'accounts/register.html', {'message':message})
        else:
            email = None
            new = User.objects.create_user(username, email, password)
            new.save()
            user = authenticate(request, username=username, password=password)
            login(request, user)
            message = "Successfully created account. You may now login."
            return render(request, 'accounts/login.html', {'message':message})
    else: 
        return render(request, 'accounts/register.html')