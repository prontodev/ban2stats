from django.contrib import admin
from attack.models import Attack


class AttackAdmin(admin.ModelAdmin):
    list_display = ('attacker_ip', 'service_name', 'geo_location', 'country_code', 'timestamp')
    search_fields = ('attacker_ip', 'service_name', 'country_code', 'geo_location')
    list_filter = ('country_code', 'service_name')

admin.site.register(Attack, AttackAdmin)