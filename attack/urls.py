from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    url(r'^new/$', 'attack.views.add_attack', name='add_attack'),
    url(r'^search/', include('haystack.urls')),
    url(r'^view/', 'attack.views.view_analytics', name='view_analytics'),
)
