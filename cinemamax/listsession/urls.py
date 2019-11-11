from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'listsession'

urlpatterns = [
	#url(r'^$', views.index, name='index'),
	path('', views.index),
	path('<int:idzal>/<int:numses>/', views.printzal),
	]
