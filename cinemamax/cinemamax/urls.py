from django.conf.urls import include, url
from django.contrib import admin
from . import views
from . import views as s
urlpatterns = [
	url(r'^listsession/', include('listsession.urls')),
    url(r'^admin/', admin.site.urls),
	url(r'^$', views.index, name='index'),
	url(r'^accounts/', include('accounts.urls')),
]
