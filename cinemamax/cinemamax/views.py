from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from maindb.models import Sessions,Buyticket,Users,Seats
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf.urls.static import static

def index(request):
    if request.method == "POST":
        typetick=request.POST.get("type")
        if(typetick==1):
            typetick=True
        else:
            typetick=False
        sid=Buyticket.objects.last().buyid+1
        un=request.user.username
        uid=Users.objects.get(uname=un).user_id
        numses=request.POST.get("nums")
        zal=request.POST.get("zal")
        lasttick=Buyticket.objects.last().sessionid
        lasttick.idsession=numses

        lastseat=Buyticket.objects.last().seatid

        lastuser=Buyticket.objects.last().userid
        lastuser.user_id=uid
        listtick=[]
        listtick= request.POST.get("listticketbuy").split(",")
        for i in range(len(listtick)-1):
                sed=Seats.objects.get(hallid=zal,num=listtick[i]).idseats
                lastseat.idseats=sed
                ticket=Buyticket(buyid=sid,sessionid=lasttick,seatid=lastseat,userid=lastuser,isbuy=typetick)
                ticket.save()
                sid+=1
    if request.user.is_authenticated:
        return render(request,"baseauth.html")
    else:
        return render(request,"base.html")

