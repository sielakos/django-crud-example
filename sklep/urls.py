from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('sklepapp.urls', namespace="sklepapp")),
    url(r'^admin/', include(admin.site.urls)),
)
