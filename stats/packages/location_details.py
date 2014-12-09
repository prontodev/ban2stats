from stats.packages.base import PackageBuilder
from haystack.query import SearchQuerySet
from django.contrib.gis.geos import Point


class LocationDetailsPackageBuilder(PackageBuilder):
    def get_objects(self, latitude, longitude):
        location = Point(longitude, latitude)
        objects = SearchQuerySet().within('location', location, location).order_by('attacked_service')
        return objects