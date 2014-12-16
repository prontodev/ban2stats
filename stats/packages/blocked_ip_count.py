from stats.packages.base import PackageBuilder
from haystack.query import SearchQuerySet
from attack.models import Attack
from django.db.models import Count


class BlockedIPCountPackageBuilder(PackageBuilder):
    def get_object(self):
        count = Attack.objects.distinct('attacker_ip').count()
        return count

    def render(self):
        count_as_string = "{:,}".format(self.get_object())
        json = '{{"count":"{0}"}}'.format(count_as_string)
        return json