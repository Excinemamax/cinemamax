from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from maindb.models import Sessions

def index(request):
        ses=Sessions.objects.all()
        return render(request,"seslist/index.html",{"ses_lst":Sessions.objects.all()})
