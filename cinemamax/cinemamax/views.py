from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from maindb.models import Sessions
from django.shortcuts import render, redirect

def index(request):
        return render(request,"base.html")
