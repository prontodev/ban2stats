from unittest import TestCase
from subprocess import call


class ShellScriptTest(TestCase):

    def test_run_script(self):
        call(['./webservice_client.py', 'poor_service', 'http', '8000', '72.14.207.99'])