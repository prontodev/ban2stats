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