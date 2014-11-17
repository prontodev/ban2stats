from django.test import TestCase
from django.http.request import HttpRequest
from ban2stats_v2.decorators import token_required



@token_required
def function_for_testing(request, x):
    return x


class TestTokenRequired(TestCase):

    def test_token_success(self):
        request = HttpRequest()
        request.META = {'HTTP_TOKEN': 'oTbCmV71i2Lg5wQMSsPEFKGJ0Banana'}
        result = function_for_testing(request, 'echome')
        self.assertEqual(result, 'echome')

    def test_token_fail__required(self):
        request = HttpRequest()
        request.META = {}
        response = function_for_testing(request, 'echome')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, 'Token is required/mismatched.')

    def test_token_fail__mismatched(self):
        request = HttpRequest()
        request.META = {'HTTP_TOKEN': 'Banana'}
        response = function_for_testing(request, 'echome')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, 'Token is required/mismatched.')

