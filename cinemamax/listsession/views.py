from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from maindb.models import Sessions,Film,Buyticket,Seats,Users
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
import datetime
from django.db.models import Count
import time

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
                     return render(request,"seslist/calendar.html",{"datenow":datetime.datetime.now().strftime("%Y-%m-%d")})

def printzal(request,idzal,numses):
        if request.user.is_authenticated:
                if((Users.objects.get(uname=request.user.username).card)is None):
                        isbuy=0
                else:
                        isbuy=1
                datetimeses=Sessions.objects.get(idsession=numses).datasession
                isres=1
                endbuy=1
                print(datetime.datetime.now())
                print(datetimeses)
                deltatime=(datetimeses-datetime.datetime.now()).seconds/60
                prosh=(datetime.datetime.now()-datetimeses).seconds/60
                if (abs(deltatime)<=60 and datetime.datetime.now().day==datetimeses.day and datetime.datetime.now().month==datetimeses.month ):
                        Buyticket.objects.filter(sessionid=numses,isbuy=False).delete()
                        isres=0
                if (abs(deltatime)<=30 and datetime.datetime.now().day==datetimeses.day and datetime.datetime.now().month==datetimeses.month):
                        endbuy=0
                if(datetime.datetime.now().day>datetimeses.day and datetime.datetime.now().month==datetimeses.month or ((datetime.datetime.now()-datetimeses).seconds/60 >0) and (datetime.datetime.now().day==datetimeses.day)):
                        isres=0
                        endbuy=0
                
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
                #return render(request,zal,{"buylist":buylist,"sizelist":sizelist,"numses":numses,"zal":idzal,"reslist":reslist,"sizeres":sizeres})
                return render(request,"seslist/zal1.html",{"buylist":buylist,"sizelist":sizelist,"numses":numses,"zal":idzal,"reslist":reslist,"sizeres":sizeres,"isb":isbuy,"isress":isres,"endbuy":endbuy})
        else:
                return render(request,"seslist/logged_out.html")

def endbuy(request):
        return render(request,"seslist/endbuy.html")
