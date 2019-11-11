from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from maindb.models import Sessions
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

def index(request,productid):
        ses=Sessions.objects.all()
        username = request.user.username
        print(username)
        return render(request,"seslist/index.html",{"ses_lst":Sessions.objects.all()})

