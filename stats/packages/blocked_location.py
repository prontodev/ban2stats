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

    def format_last_seen_string(self, last_seen_raw):
        if last_seen_raw is None:
            return 'n/a'
        last_seen_datetime = parse(last_seen_raw)
        return last_seen_datetime.strftime("%b %d, %Y %H:%M:%S %z")

    def render_each_object(self, object):
        latitude, longitude = eval(object[0])
        data = {'latitude':latitude, 'longitude':longitude, 'count':object[1]}
        template = '''["{latitude}","{longitude}",{count}]'''
        output_string = template.format(**data)
        return output_string

    def render_as_javascript(self):
        template = """
        "blocked_ips": {0},\n
        "blocked_ip_count": "{1}"
        """
        return template.format(self.render_all_objects_as_list(), self.objects_count_as_string(len(self.objects)))


