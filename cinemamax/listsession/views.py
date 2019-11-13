from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from maindb.models import Sessions,Film,Buyticket,Seats,Users
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
import datetime
from django.db.models import Count


def index(request):
        if request.method == "POST":
                listtick = request.POST.get("List")
                return render(request,"seslist/calendar.html",{"datenow":datetime.date.today()})
        else:
                ourday=request.GET.get("calendar")
                if ourday!=None:
                        beginourday=request.GET.get("calendar")+" 00:00:00.0"
                        endourday=request.GET.get("calendar")+" 23:59:59.0"
                        #ourday=request.GET.get("calendar")
                        timeBegin=datetime.datetime.strptime(beginourday,'%Y-%m-%d %H:%M:%S.%f')
                        timeEnd=datetime.datetime.strptime(endourday,'%Y-%m-%d %H:%M:%S.%f')
                        sestoday=Sessions.objects.filter(datasession__gte=timeBegin,datasession__lte=timeEnd).order_by('fillname')
                        cnt=Sessions.objects.filter(datasession__gte=timeBegin,datasession__lte=timeEnd).order_by('fillname').values('fillname').annotate(dcount=Count('fillname')).count()
                        sesgroup=Sessions.objects.filter(datasession__gte=timeBegin,datasession__lte=timeEnd).distinct('fillname')
                        listses=[]
                        listnamefilm=[]
                        listimg=[]
                        for i in range(cnt):
                                listses.append(Sessions.objects.select_related().filter(datasession__gte=timeBegin,datasession__lte=timeEnd,fillname=sesgroup[i].fillname))
                                print(listses[i][0].fillname.imgurl)
                        for i in range(cnt):
                                listimg.append(Film.objects.get(namefilm=listses[i][0].fillname.namefilm).imgurl)
                        return render(request,"seslist/rasp.html",{"listses":listses,"imglist":listimg})
                #cur_user=request.user
                #if (cur_user.is_authenticated):
                        #print("Hellow user",request.user.username)	
                #return render(request,"seslist/calendar.html")
                else:
                     x=Sessions.objects.select_related ('fillname')
                     for s in x:
                             print(s.fillname.imgurl)
                     return render(request,"seslist/calendar.html",{"datenow":datetime.date.today()})

def printzal(request,idzal,numses):
        if request.user.is_authenticated:
                if((Users.objects.get(uname=request.user.username).card)is None):
                        zal="seslist/zalres"+str(idzal)
                else:
                        zal="seslist/zal"+str(idzal)
                zal=zal+".html"
                Select_numses=Buyticket.objects.filter(sessionid=numses,isbuy=True)
                Select_numsesreserv=Buyticket.objects.filter(sessionid=numses,isbuy=False)
                reslist=[]
                buylist=[]
                sizelist=0
                sizeres=0
                for i in Select_numses:
                        buylist.append(Seats.objects.get(idseats=i.seatid.idseats).num)
                        sizelist+=1
                for i in Select_numsesreserv:
                        reslist.append(Seats.objects.get(idseats=i.seatid.idseats).num)
                        sizeres+=1
                return render(request,zal,{"buylist":buylist,"sizelist":sizelist,"numses":numses,"zal":idzal,"reslist":reslist,"sizeres":sizeres})
        else:
                return render(request,"seslist/logged_out.html")

def endbuy(request):
        return render(request,"seslist/endbuy.html")
