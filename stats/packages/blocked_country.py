from stats.packages.base import PackageBuilder
from haystack.query import SearchQuerySet
import json


class BlockedCountryPackageBuilder(PackageBuilder):

    def get_objects(self):
        country_search_queryset = SearchQuerySet().facet('country_name', order='count')
        countries = country_search_queryset.facet_counts()['fields']['country_name']
        return countries

    def render_each_object(self, object):
        count_as_string = "{:,}".format(object[1])
        data_dict = dict(country_name=object[0], count=count_as_string)
        return json.dumps(data_dict)

    def render_as_javascript(self):
        template = """
        "blocked_countries": {0}"""
        return template.format(self.render_all_objects_as_list())

