from unittest import TestCase
from webservice_client import BAN2STATSHandler
import mock


class ClientTest(TestCase):

    def test_api_url(self):
        handler = BAN2STATSHandler()
        handler.WEBSERVICE_HOST = "http://WebService_HOST:8000"
        handler.BAN2STATS_HANDLER_URL = "/test_handler_url/"
        self.assertEqual(handler.api_url(), 'http://WebService_HOST:8000/test_handler_url/')

    def test_api_headers(self):
        handler = BAN2STATSHandler()
        self.assertEqual(handler.api_headers()['Token'], 'Banana')

    @mock.patch('httplib2.Http.request')
    def test_call_webservice_api(self, mock_http):
        mock_http.return_value = (200, 'ACK from Webservice')
        handler = BAN2STATSHandler()
        test_url = 'http://localhost:8000/some_url/'
        response_code, response_content = handler.call_webservice_api(test_url, {'data': 'data'})
        self.assertEqual(response_code, 200)
        self.assertEqual(response_content, 'ACK from Webservice')

    @mock.patch('httplib2.Http.request')
    def test_call_ban2stats_handler_api(self, mock_http):
        mock_http.return_value = (200, 'Saved Ban record.')
        handler = BAN2STATSHandler()
        response = handler.call_ban_handler({})
        self.assertEqual(response[0], 200)
        self.assertEqual(response[1], 'Saved Ban record.')