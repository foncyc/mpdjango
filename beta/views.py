# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.conf import settings

def show_beta(request):
    return render(request, 'beta/beta.html')    

def show_error(request):
    return render(request, 'beta/beta_error.html')

def show_logout(request):

    message = "Successfully logged out!"
    return render(request, 'beta/beta_loggedout.html', {'message':message})
