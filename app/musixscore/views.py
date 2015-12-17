from django.shortcuts import render
from django.http import *
from django.views.generic import View
from django.contrib import auth
from models import *
from forms import *
import json
from django.utils import timezone
import datetime
from django.db import connection
# Create your views here.


def index(request):
    form = LoginForm()
    return render(request, 'index.html', {'form': form})


class Login(View):
    def post(self, request):
        form = LoginForm(self.request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponse('Logged In!')
            else:
                return HttpResponse('Invalid pasword/username!')
        else:
            return HttpResponse('Please fill out required forms!')


def addGenre(request):
    return render(request, 'add_genre.html')