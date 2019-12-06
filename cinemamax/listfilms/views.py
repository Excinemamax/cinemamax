from django.shortcuts import render
from maindb.models import Film,Sessions

def index(request):
        listses=Sessions.objects.all()
        listname=[]
        for i in listses:
                listname.append(i.fillname.namefilm)
        films=Film.objects.filter(namefilm__in = listname)
        for i in films:
                print (i.namefilm)
        print("END")
        film_in=[]
        films_all=Film.objects.all()
        for i in films_all:
                film_in.append(i.namefilm)
        films_notin=Film.objects.filter(namefilm__in = (set(film_in)-set(listname)))
        print(films_notin[0].namefilm)
        return render(request,"filmlist/index.html",{"film_lst":films,"film_not":films_notin})

def onefilm(request,filmid):
        film=Film.objects.get(namefilm=filmid)
        print(film.namefilm)
        return render(request,"filmlist/kino.html",{"film":film})
			
