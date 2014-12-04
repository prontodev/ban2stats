from django.db import models
from django.contrib.gis.geos import Point


class Attack(models.Model):

    attacker_ip = models.IPAddressField()

    service_name = models.CharField(max_length=140)
    protocol = models.CharField(max_length=140)
    port = models.CharField(max_length=140)

    latitude = models.FloatField()
    longitude = models.FloatField()
    country_code = models.CharField(max_length=3)
    geo_location = models.CharField(max_length=140)
    timestamp = models.DateTimeField()

    def get_location(self):
        # Remember, longitude FIRST!
        return Point(self.longitude, self.latitude)