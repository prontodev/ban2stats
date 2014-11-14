from unittest import TestCase
from subprocess import call


class ShellScriptTest(TestCase):

    def test_run_script(self):
        call(['./webservice_client.py', 'poor_service', 'http', '80', '127.0.0.1'])