from stats.packages.base import PackageBuilder
from haystack.query import SearchQuerySet
from dateutil.parser import parse
from django.contrib.gis.geos import Point


class BlockedLocationPackageBuilderMinimized(PackageBuilder):

    def __init__(self):
        self.objects = []

    def get_objects(self):
        blocked_ip_list = SearchQuerySet().facet('location').facet_counts()['fields']['location']
        self.objects = blocked_ip_list
        return blocked_ip_list

    def render_each_object(self, object):
        latitude, longitude = eval(object[0])
        data = {'latitude':latitude, 'longitude':longitude, 'count':object[1]}
        template = '''["{latitude}","{longitude}",{count}]'''
        output_string = template.format(**data)
        return output_string
