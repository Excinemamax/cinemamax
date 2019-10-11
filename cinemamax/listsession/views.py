from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from maindb.models import Sessions

def index(request):
        ses=Sessions.objects.all()
        return HttpResponse(ses[0].fillname)
