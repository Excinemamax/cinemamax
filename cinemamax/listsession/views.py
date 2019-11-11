from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from maindb.models import Sessions,Film,Buyticket,Seats
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
import datetime
from django.db.models import Count

def index(request):
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
                        listses.append(Sessions.objects.filter(datasession__gte=timeBegin,datasession__lte=timeEnd,fillname=sesgroup[i].fillname))
                        print(Sessions.objects.filter(datasession__gte=timeBegin,datasession__lte=timeEnd,fillname=sesgroup[i].fillname))
                for i in range(cnt):
                        for j in listses[i]:
                                print(j.fillname)
                        print("ENDLLL")
                for i in range(cnt):
                        listimg.append(Film.objects.get(namefilm=listses[i][0].fillname.namefilm).imgurl)
                        print(listimg[i])
                print("Номер зала",listses[0][0].numberhall.idhall)
                return render(request,"seslist/rasp.html",{"listses":listses,"imglist":listimg})
        #cur_user=request.user
        #if (cur_user.is_authenticated):
                #print("Hellow user",request.user.username)	
        #return render(request,"seslist/calendar.html")
        else:
             print("hellow")
             return render(request,"seslist/calendar.html",{"datenow":datetime.date.today()})

def printzal(request,idzal,numses):
        zal="seslist/zal"+str(idzal)
        zal=zal+".html"
        Select_numses=Buyticket.objects.filter(sessionid=numses)
        buylist=[]
        sizelist=0
        for i in Select_numses:
                buylist.append(Seats.objects.get(idseats=i.seatid.idseats).num)
                sizelist+=1
                print(i.seatid.idseats)
        return render(request,zal,{"buylist":buylist,"sizelist":sizelist})
