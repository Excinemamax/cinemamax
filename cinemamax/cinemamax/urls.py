from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
	url(r'^listsession/', include('listsession.urls')),
    url(r'^admin/', admin.site.urls),
	url(r'^$', views.index, name='index'),
	url(r'^accounts/', include('accounts.urls')),
	url(r'^listfilms/', include('listfilms.urls')),
]
