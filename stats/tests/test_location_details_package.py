from django.test import TestCase
from attack.models import Attack
from django.core.management import call_command
from stats.packages.location_details import LocationDetailsPackageBuilder


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
        self.item2 = Attack.objects.create(**{
                "attacker_ip": "72.14.207.99",
                "service_name": "HR Portal",
                "longitude": -122.057403564,
                "geo_location": "CA, United States",
                "country_name": "United States",
                "timestamp": "2014-10-18T12:58:56.106Z",
                "latitude": 37.4192008972,
                "protocol": "https",
                "port": "8333",
             })
        self.item3 = Attack.objects.create(**{
                "attacker_ip": "72.14.207.100",
                "service_name": "HR Portal",
                "longitude": -122.057403564,
                "geo_location": "CA, United States",
                "country_name": "United States",
                "timestamp": "2014-12-30T12:58:56.106Z",
                "latitude": 37.4192008972,
                "protocol": "https",
                "port": "8333",
             })
        call_command('rebuild_index', interactive=False, verbosity=0)
        self.builder = LocationDetailsPackageBuilder(37.4192008972, -122.057403564)

    def test_get_objects(self):
        location_list = self.builder.get_objects()
        self.assertEqual(len(location_list), 2)

        ip_99 = filter(lambda x: x[0] == "72.14.207.99", location_list)[0]
        self.assertEqual(ip_99[0], u"72.14.207.99")
        self.assertEqual(ip_99[1], 2)
        ip_100 = filter(lambda x: x[0] == "72.14.207.100", location_list)[0]
        self.assertEqual(ip_100[0], u"72.14.207.100")
        self.assertEqual(ip_100[1], 1)

    def test_render_each_object(self):
        location_list = self.builder.get_objects()
        ip_99 = filter(lambda x: x[0] == "72.14.207.99", location_list)[0]
        content = self.builder.render_each_object(ip_99)
        expected_content = '''["Internal Wordpress System","72.14.207.99","2014-11-18T12:58:56",2]'''
        self.assertEqual(content, expected_content)

    def test_render_all_objects(self):
        content = self.builder.render_all_objects_as_list()
        self.assertIn('''[\n[''', content)
        self.assertIn(''']\n]''', content)
