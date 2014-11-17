from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^new/$', 'attack.views.add_attack', name='add_attack'),

)
