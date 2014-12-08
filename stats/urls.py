from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'stats.views.get_stats', name='get_stats'),
    url(r'^attacked_services/$', 'stats.views.get_attacked_services', name='get_attacked_services'),
    url(r'^blocked_countries/$', 'stats.views.get_blocked_countries', name='get_blocked_countries'),
    url(r'^blocked_ips/$', 'stats.views.get_blocked_ips', name='get_blocked_ips'),
)