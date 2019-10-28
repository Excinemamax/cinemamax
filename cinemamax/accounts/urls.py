from django.contrib.auth import views
from django.urls import path
from django.conf.urls import include, url
from . import views as s

urlpatterns = [
	path('login/', views.LoginView.as_view(), name='login'),
	path('logout/', views.LogoutView.as_view(), name='logout'),
	url(r'^signup/$', s.signup, name='signup'),
]