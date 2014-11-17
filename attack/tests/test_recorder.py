from django.test import TestCase
from attack.recorder import AttackRecorder


class TestRecorder(TestCase):

    def setUp(self):
        self.attack_recorder = AttackRecorder()

    def test_get_geo_data(self):
        ip = '72.14.207.99'
        geo_details = self.attack_recorder.get_geo_data(ip=ip)
        self.assertEqual(self.attack_recorder.data['country'], u'US')
        self.assertEqual(self.attack_recorder.data['geo_location'], u'CA, United States')