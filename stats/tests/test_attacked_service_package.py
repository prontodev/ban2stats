from django.test import TestCase
from attack.models import Attack
from stats.packages.attacked_service import AttackedServicePackageBuilder
from django.core.management import call_command


class TestGetAttackedServiceStats(TestCase):

    def setUp(self):

        for i in xrange(0, 1123):
            self.item1 = Attack.objects.create(**{
                "attacker_ip": "72.14.207.99",
                "service_name": "Internal Wordpress System",
                "longitude": -122.057403564,
                "geo_location": "CA, United States",
                "country_code": "US",
                "timestamp": "2014-11-18T12:58:56.106Z",
                "latitude": 37.4192008972,
                "protocol": "http",
                "port": "2333",
             })

        for i in xrange(0, 3):
            Attack.objects.create(**{
                "attacker_ip": "72.14.207.99",
                "service_name": "Mail Server",
                "longitude": -122.057403564,
                "geo_location": "CA, United States",
                "country_code": "US",
                "timestamp": "2014-11-18T12:58:56.106Z",
                "latitude": 37.4192008972,
                "protocol": "http",
                "port": "2333"
            })
            
        for i in xrange(0, 1563):
            Attack.objects.create(**{
                "attacker_ip": "72.14.207.99",
                "service_name": "Company Secured Server",
                "longitude": -122.057403564,
                "geo_location": "CA, United States",
                "country_code": "US",
                "timestamp": "2014-11-18T12:58:56.106Z",
                "latitude": 37.4192008972,
                "protocol": "http",
                "port": "2333"
            })

        call_command('rebuild_index', interactive=False, verbosity=0)
        self.attacked_services = AttackedServicePackageBuilder()

    def test_get_attacked_services(self):
        objects = self.attacked_services.get_objects()
        self.assertEqual(len(objects), 3)

    def test_render_each_object(self):
        content = self.attacked_services.render_each_object(["Internal Wordpress System", 1])
        self.assertEqual(content, u'["Internal Wordpress System", 1]')

    def test_render_all_objects(self):
        content = self.attacked_services.render_all_objects()
        expected_content = u'''["Internal Wordpress System", 1123]'''
        self.assertIn(expected_content, content)
        expected_content = u'''["Mail Server", 3]'''
        self.assertIn(expected_content, content)
        expected_content = u'''["Company Secured Server", 1563]'''
        self.assertIn(expected_content, content)
        self.assertNotEqual(",", content[-1])

    def test_render_javascript(self):
        content = self.attacked_services.render_as_javascript()
        expected_content = u'''["Internal Wordpress System", 1123]'''
        self.assertIn(expected_content, content)
        expected_content = u'''["Mail Server", 3]'''
        self.assertIn(expected_content, content)
        expected_content = u'''["Company Secured Server", 1563]'''
        self.assertIn(expected_content, content)
        expected_content = u'''"attacked_services": ['''
        self.assertIn(expected_content, content)
        expected_content = u''']'''
        self.assertIn(expected_content, content)