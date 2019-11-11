from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from maindb.models import Sessions
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf.urls.static import static

def index(request):
    if request.user.is_authenticated:
        return render(request,"baseauth.html")
    else:
        return render(request,"base.html")

