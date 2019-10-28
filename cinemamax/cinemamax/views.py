from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from maindb.models import Sessions
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def index(request):
        return render(request,"base.html")

