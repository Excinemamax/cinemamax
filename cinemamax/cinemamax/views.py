from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from maindb.models import Sessions,Buyticket,Users,Seats
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf.urls.static import static
import datetime

def index(request):
    if request.method == "POST":
        typetick=request.POST.get("type")
        print(typetick,type(typetick))
        if(typetick=="1"):
            typetick=True
        else:
            typetick=False
        print("Куплено или",typetick)
        if(Buyticket.objects.all().count()!=0):
            sid=Buyticket.objects.last().buyid+1
        else:
            sid=1
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

def cont(request):
    return render (request,"seslist/conts.htnl")

def myticket(request):
    if (not (request.user.is_authenticated)):
        return render(request,"seslist/endbuy.html")
    else:
        listrow=[]
        listcol=[]
        endses=[]
        noend=[]
        ses_end=Sessions.objects.all()
        for i in ses_end:
            if i.datasession<datetime.datetime.now():
                endses.append(i.idsession)
        #Buyticket.objects.filter(sessionid__in=endses).delete()
        for i in ses_end:
            noend.append(i.idsession)
        noend=list(set(noend)-set(endses))
        id_user=Users.objects.get(uname=request.user.username).user_id
        mytickets=Buyticket.objects.select_related().filter(userid=id_user,sessionid__in=noend)
        oneplace=zip(mytickets,listrow,listcol)
        for i in mytickets:
            if (i.seatid.hallid.idhall==1):
                if(i.seatid.num>0 and i.seatid.num<6):
                    listrow.append(1)
                    listcol.append(i.seatid.num)
                elif(i.seatid.num>5 and i.seatid.num<13):
                    listrow.append(2)
                    listcol.append(i.seatid.num-5)
                elif(i.seatid.num>12 and i.seatid.num<22):
                    listrow.append(3)
                    listcol.append(i.seatid.num-12)
                elif(i.seatid.num>21 and i.seatid.num<31):
                    listrow.append(4)
                    listcol.append(i.seatid.num-21)
                elif(i.seatid.num>30 and i.seatid.num<40):
                    listrow.append(5)
                    listcol.append(i.seatid.num-30)
                elif(i.seatid.num>39 and i.seatid.num<49):
                    listrow.append(6)
                    listcol.append(i.seatid.num-39)
                elif(i.seatid.num>48 and i.seatid.num<58):
                    listrow.append(7)
                    listcol.append(i.seatid.num-48)   
            elif (i.seatid.hallid.idhall==2):
                if(i.seatid.num>0 and i.seatid.num<6):
                    listrow.append(1)
                    listcol.append(i.seatid.num)
                elif(i.seatid.num>5 and i.seatid.num<13):
                    listrow.append(2)
                    listcol.append(i.seatid.num-5)
                elif(i.seatid.num>12 and i.seatid.num<22):
                    listrow.append(3)
                    listcol.append(i.seatid.num-12)
            elif (i.seatid.hallid.idhall==3):
                if(i.seatid.num>0 and i.seatid.num<6):
                    listrow.append(1)
                    listcol.append(i.seatid.num)
                elif(i.seatid.num>5 and i.seatid.num<13):
                    listrow.append(2)
                    listcol.append(i.seatid.num-5)
                elif(i.seatid.num>12 and i.seatid.num<22):
                    listrow.append(3)
                    listcol.append(i.seatid.num-12)
                elif(i.seatid.num>21 and i.seatid.num<31):
                    listrow.append(4)
                    listcol.append(i.seatid.num-21)
                elif(i.seatid.num>30 and i.seatid.num<40):
                    listrow.append(5)
                    listcol.append(i.seatid.num-30)
                elif(i.seatid.num>39 and i.seatid.num<49):
                    listrow.append(6)
                    listcol.append(i.seatid.num-39)
                elif(i.seatid.num>48 and i.seatid.num<58):
                    listrow.append(7)
                    listcol.append(i.seatid.num-48)
                elif(i.seatid.num>57 and i.seatid.num<68):
                    listrow.append(8)
                    listcol.append(i.seatid.num-57)
                elif(i.seatid.num>67 and i.seatid.num<79):
                    listrow.append(9)
                    listcol.append(i.seatid.num-67)
            
    return render (request,"myticket/myticket.html",{"tick":oneplace})
