from django.test import TestCase
from attack.models import Attack
from django.db.models import ObjectDoesNotExist


class TestAttackAdd(TestCase):

    def setUp(self):
        self.request_headers = {'HTTP_TOKEN': 'oTbCmV71i2Lg5wQMSsPEFKGJ0Banana'}

    def test_add_fail__invalid_IP(self):
        fail2ban_data = dict(
            attacker_ip='127.8.8.8',
            service_name='company web server test view: invalid ip',
            protocol='http',
            port='82',
        )
        response = self.client.post('/attack/new/', data=fail2ban_data, **self.request_headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, 'Cannot find Geo details for this IP 127.8.8.8')
        self.assertRaises(ObjectDoesNotExist, Attack.objects.get, attacker_ip='127.8.8.8', port='81')

    def test_add_fail__missing_parameter(self):
        fail2ban_data = dict()
        response = self.client.post('/attack/new/', data=fail2ban_data, **self.request_headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, 'Required attacker_ip, service_name, protocol and port.')
        self.assertRaises(ObjectDoesNotExist, Attack.objects.get, attacker_ip='72.14.207.99', port='81')

    def test_add(self):
        fail2ban_data = dict(
            attacker_ip='72.14.207.99',
            service_name='company web server test view',
            protocol='http',
            port='81',
        )
        response = self.client.post('/attack/new/', data=fail2ban_data, **self.request_headers)

        attacks_from_db = Attack.objects.get(attacker_ip='72.14.207.99', port='81')
        self.assertEqual(attacks_from_db.service_name, 'company web server test view')
        self.assertEqual(attacks_from_db.port, '81')
        self.assertEqual(attacks_from_db.country_code, u'US')
        self.assertEqual(attacks_from_db.geo_location, u'CA, United States')
        self.assertEqual(attacks_from_db.latitude, u'37.4192008972')
        self.assertEqual(attacks_from_db.longitude, u'-122.057403564')

        self.assertContains(response, 'Added attack')
