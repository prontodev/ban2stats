from django.test import TestCase
from django.contrib.auth.models import User


class TestAttackAdmin(TestCase):

    def create_superuser(self):
        User.objects.create_superuser('iamadmin', 'admin@example.com', 'iamadmin')

    def setUp(self):
        self.create_superuser()
        self.client.login(username='iamadmin',password='iamadmin')

    def test_list_page(self):
        response = self.client.get('/admin/attack/attack/')
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        response = self.client.get('/admin/attack/attack/?q=this-ip')
        self.assertEqual(response.status_code, 200)