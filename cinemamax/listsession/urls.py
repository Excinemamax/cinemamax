from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'listsession'

urlpatterns = [
	path('<int:productid>/', views.index),
	]
