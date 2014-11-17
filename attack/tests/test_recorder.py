from django.test import TestCase
from attack.recorder import AttackRecorder
from attack.models import Attack


class TestRecorder(TestCase):

    def setUp(self):
        self.attack_recorder = AttackRecorder()

    def test_get_geo_data(self):
        ip = '72.14.207.99'
        geo_details = self.attack_recorder.get_geo_data(ip=ip)
        self.assertEqual(self.attack_recorder.data['country_code'], u'US')
        self.assertEqual(self.attack_recorder.data['geo_location'], u'CA, United States')

    def test_get_geo_data_invalid_ip(self):
        ip = '127.8.8.8'
        self.assertRaisesMessage(ValueError, 'Cannot find Geo details for this IP 127.8.8.8',
                                 self.attack_recorder.get_geo_data, ip=ip )

    def test_stamp_time(self):
        self.attack_recorder.stamp_time()
        self.assertTrue(self.attack_recorder.data['timestamp'])

    def test_record_save(self):
        self.attack_recorder.set_data(attacker_ip='72.14.207.99',
                        service_name='company web server',
                        protocol='http',
                        port='80',)
        self.attack_recorder.get_geo_data()
        self.attack_recorder.stamp_time()
        saved_attack = self.attack_recorder.save()
        self.assertEqual(saved_attack.service_name, 'company web server')
        self.assertEqual(saved_attack.country_code, 'US')

    def test_set_data_with_empty_values(self):
        self.assertRaisesMessage(ValueError, 'Required attacker_ip, service_name, protocol and port.', self.attack_recorder.set_data)