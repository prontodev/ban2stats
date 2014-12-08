from django.test import TestCase
from attack.models import Attack
from stats.packages.blocked_country import BlockedCountryPackageBuilder
from django.core.management import call_command


class TestBlockedCountryPackageBuilder(TestCase):

    def setUp(self):
        for i in xrange(0, 22):
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

        for i in xrange(0, 1000):
            self.item2 = Attack.objects.create(**{
                "attacker_ip": "72.14.207.99",
                "service_name": "Internal Wordpress System",
                "longitude": -122.057403564,
                "geo_location": "Thailand",
                "country_name": "Thailand",
                "timestamp": "2014-11-18T12:58:56.106Z",
                "latitude": 37.4192008972,
                "protocol": "http",
                "port": "2333",
             })

        for i in xrange(0, 1111):
            self.item3 = Attack.objects.create(**{
                "attacker_ip": "72.14.207.99",
                "service_name": "Internal Wordpress System",
                "longitude": -122.057403564,
                "geo_location": "Singapore",
                "country_name": "Singapore",
                "timestamp": "2014-11-18T12:58:56.106Z",
                "latitude": 37.4192008972,
                "protocol": "http",
                "port": "2333",
             })

        for i in xrange(0, 3):
            self.item4 = Attack.objects.create(**{
                "attacker_ip": "72.14.207.99",
                "service_name": "Internal Wordpress System",
                "longitude": -122.057403564,
                "geo_location": "Albania",
                "country_name": "Albania",
                "timestamp": "2014-11-18T12:58:56.106Z",
                "latitude": 37.4192008972,
                "protocol": "http",
                "port": "2333",
             })

        for i in xrange(0, 1123):
            self.item4 = Attack.objects.create(**{
                "attacker_ip": "72.14.207.99",
                "service_name": "Internal Wordpress System",
                "longitude": -122.057403564,
                "geo_location": "Morocco",
                "country_name": "Morocco",
                "timestamp": "2014-11-18T12:58:56.106Z",
                "latitude": 37.4192008972,
                "protocol": "http",
                "port": "2333",
             })

        for i in xrange(0, 50):
            self.item5 = Attack.objects.create(**{
                "attacker_ip": "72.14.207.99",
                "service_name": "Internal Wordpress System",
                "longitude": -122.057403564,
                "geo_location": "Peru",
                "country_name": "PE",
                "timestamp": "2014-11-18T12:58:56.106Z",
                "latitude": 37.4192008972,
                "protocol": "http",
                "port": "2333",
             })

        call_command('rebuild_index', interactive=False, verbosity=0)
        self.builder = BlockedCountryPackageBuilder()

    def test_render_each_object(self):
        object = self.builder.get_objects()[0] #(u'Morocco', 1123)
        content = self.builder.render_each_object(object)
        self.assertIn('{', content)
        self.assertIn('"country_name": "Morocco"', content)
        self.assertIn('"count": "1,123"', content)
        self.assertIn('}', content)

    def test_render_all_objects(self):
        content = self.builder.render_all_objects()
        self.assertIn('{', content)
        self.assertIn('"country_name": "Morocco"', content)
        self.assertIn('"count": "1,123"', content)
        self.assertIn('}', content)
        self.assertNotEqual(',', content[-1])

    def test_render_as_javascript(self):
        content = self.builder.render_as_javascript()

        expected_content = u''']'''
        self.assertIn(expected_content, content)