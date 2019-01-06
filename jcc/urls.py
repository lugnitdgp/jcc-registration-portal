from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from core.views import Team_List

urlpatterns = [
    url(r'^teams', Team_List, name='Team'),
    url(r'^admin', admin.site.urls),
    url(r'^', include('core.urls')),
]
