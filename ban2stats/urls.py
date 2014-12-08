from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^attack/', include('attack.urls')),
    url(r'^stats/', include('stats.urls')),
)
