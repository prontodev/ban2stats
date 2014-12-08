from django.contrib import admin
from attack.models import Attack


class AttackAdmin(admin.ModelAdmin):
    list_display = ('attacker_ip', 'service_name', 'geo_location', 'country_name', 'timestamp')
    search_fields = ('attacker_ip', 'service_name', 'country_name', 'geo_location')
    list_filter = ('country_name', 'service_name')

admin.site.register(Attack, AttackAdmin)