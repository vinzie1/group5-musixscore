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
    return render(request, 'index.html')


class Login(View):
    def post(self, request):
        return HttpResponse()