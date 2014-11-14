#!/usr/bin/env python
import sys
from httplib2 import Http
from urllib import urlencode
from urlparse import urljoin


class BAN2STATSHandler(object):

    WEBSERVICE_HOST = 'http://localhost:8000'
    BAN2STATS_HANDLER_URL = '/attack/new/'
    TOKEN = 'oTbCmV71i2Lg5wQMSsPEFKGJ0Banana'

    def __init__(self, token=None):
        self.token = token

    def api_url(self):
        return urljoin(self.WEBSERVICE_HOST, self.BAN2STATS_HANDLER_URL)

    def api_headers(self):
        headers = {'Content-type': 'application/x-www-form-urlencoded',
                   'Token': self.TOKEN}
        return headers

    def call_webservice_api(self, url, content_data_as_dict):
        http = Http()
        body = urlencode(content_data_as_dict)
        response, content = http.request(url, "POST", headers=self.api_headers(), body=body)
        return response, content

    def call_ban_handler(self, ban2stats_data):
        response, content = self.call_webservice_api(self.api_url(), ban2stats_data)
        return response, content


if __name__ == '__main__':
    ban_handler_data = dict(
        service_name=sys.argv[1],
        protocol=sys.argv[2],
        port=sys.argv[3],

        attacker_ip=sys.argv[4],
    )

    response_headers, response_content = BAN2STATSHandler().call_ban_handler(ban_handler_data)
    print ("Banned IP {2} : {0}, {1}".format(response_headers.status, response_content, ban_handler_data['attacker_ip']))