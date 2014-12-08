from stats.packages.base import PackageBuilder
from haystack.query import SearchQuerySet


class AttackedServicePackageBuilder(PackageBuilder):

    def get_objects(self):
        attacked_service_search_queryset = SearchQuerySet().facet('attacked_service')
        attacked_services = attacked_service_search_queryset.facet_counts()['fields']['attacked_service']
        return attacked_services

    def render_each_object(self, object):
        return u"""["{0}", {1}]""".format(object[0], object[1])

    def render_as_javascript(self):
        template = """
        "attacked_services": {0}"""
        return template.format(self.render_all_objects_as_list())