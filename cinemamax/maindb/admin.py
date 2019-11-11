from django.contrib import admin
from .models import Film,Users,Sessions,Filmgenre,Genre,Seats,Buyticket,Hall

admin.site.register(Film)
admin.site.register(Users)
admin.site.register(Sessions)
admin.site.register(Filmgenre)
admin.site.register(Genre)
admin.site.register(Seats)
admin.site.register(Buyticket)
admin.site.register(Hall)