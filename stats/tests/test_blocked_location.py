from django.test import TestCase
from attack.models import Attack
from django.core.management import call_command
from stats.packages.blocked_location import BlockedLocationPackageBuilderMinimized


class TestBlockedIPPackageMinimized(TestCase):

    def setUp(self):
        self.item1 = Attack.objects.create(**{
                "attacker_ip": "72.14.207.99",
                "service_name": "Internal Wordpress System",
                "longitude": -122.057403564,
                "geo_location": "CA, United States",
                "country_name": "United States",
                "timestamp": "2014-11-18T12:58:56.106Z",
                "latitude": 37.4192008972,
                "protocol": "http",
                "port": "2333",
             })
        call_command('rebuild_index', interactive=False, verbosity=0)
        self.builder = BlockedLocationPackageBuilderMinimized()

    def test_get_objects(self):
        location_list = self.builder.get_objects()
        self.assertEqual(location_list, [(u'[37.4192008972, -122.057403564]', 1)])

    def test_render_each_object(self):
        content = self.builder.render_each_object((u'[37.4192008972, -122.057403564]', 1))
        expected_content = expected_content = '''["37.4192008972","-122.057403564",1]'''
        self.assertEqual(content, expected_content)