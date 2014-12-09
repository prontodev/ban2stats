from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^attacked_services/$', 'stats.views.get_attacked_services', name='get_attacked_services'),
    url(r'^blocked_countries/$', 'stats.views.get_blocked_countries', name='get_blocked_countries'),
    url(r'^blocked_locations/$', 'stats.views.get_block_locations', name='get_blocked_locations'),
    url(r'^location_details/$', 'stats.views.get_location_details', name='get_location_details'),
)