from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^listsession/', include('listsession.urls')),
    url(r'^admin/', admin.site.urls),
]
