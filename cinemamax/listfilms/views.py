from django.shortcuts import render
from maindb.models import Film

def index(request):
        films=Film.objects.all()
        return render(request,"filmlist/index.html",{"film_lst":films})

def onefilm(request,filmid):
        film=Film.objects.get(namefilm=filmid)
        print(film.namefilm)
        return render(request,"filmlist/kino.html",{"film":film})
			
