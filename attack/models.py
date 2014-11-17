from django.db import models


class Attack(models.Model):

    attacker_ip = models.IPAddressField()

    service_name = models.CharField(max_length=140)
    protocol = models.CharField(max_length=140)
    port = models.CharField(max_length=140)

    longitude = models.CharField(max_length=30)
    latitude = models.CharField(max_length=30)
    country_code = models.CharField(max_length=3)
    geo_location = models.CharField(max_length=140)
    timestamp = models.DateTimeField()