from django.test import TestCase
from attack.recorder import AttackRecorder


class TestRecorder(TestCase):

    def setUp(self):
        self.attack_recorder = AttackRecorder()