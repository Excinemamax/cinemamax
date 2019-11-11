from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'listfilms'

urlpatterns = [
    url(r'^$', views.index, name='index'),
	path('<str:filmid>/', views.onefilm),
	]
