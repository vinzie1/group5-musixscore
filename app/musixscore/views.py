from django.shortcuts import render
from django.http import *
from django.views.generic import View
from django.contrib import auth
from musixscore.models import *
from musixscore.forms import *
import json
from django.utils import timezone
import datetime
from django.db import connection
# Create your views here.


def index(request):
    return render(request, 'index.html')


class Login(View):
    def get(self, request):
        form = LoginForm()
        error = False
        return render(request, 'login.html', {'form': form, 'error': error})

    def post(self, request):
        form = LoginForm(self.request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/dashboard')
            else:
                error = True
                message = 'Invalid password/username!'
                return render(request, 'login.html', {'form': form, 'error': error, 'message': message})
        else:
            error = True
            message = 'Please fill out all the required forms!'
            return render(request, 'login.html', {'form': form, 'error': error, 'message': message})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')