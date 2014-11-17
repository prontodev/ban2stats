from attack.models import Attack
from django.contrib.gis.geoip import GeoIP
from django.utils.timezone import get_current_timezone
from datetime import datetime


class AttackRecorder(object):
    def __init__(self):
        self.geo_details = None
        self.data = {}

    def set_data(self, attacker_ip=None, service_name=None, protocol=None, port=None):
        if not (attacker_ip and service_name and protocol and port):
            raise ValueError('Required attacker_ip, service_name, protocol and port.')
        self.data['attacker_ip'] = attacker_ip
        self.data['service_name'] = service_name
        self.data['protocol'] = protocol
        self.data['port'] = port

    def get_geo_data(self, ip=None):
        if not ip:
            ip = self.data['attacker_ip']
        geo_ip = GeoIP()
        self.geo_details = geo_ip.city(ip)
        if self.geo_details is None:
            raise ValueError("Cannot find Geo details for this IP {0}".format(ip))

        self.data['country_code'] = self.geo_details['country_code']
        self.data['country_name'] = self.geo_details['country_name']
        self.data['latitude'] = unicode(self.geo_details['latitude'])
        self.data['longitude'] = unicode(self.geo_details['longitude'])

        region = self.geo_details.get('region') or self.geo_details.get('city') or 'n/a'
        country_name = self.geo_details.get('country_name', 'n/a')
        self.data['geo_location'] = ', '.join([region, country_name])

    def stamp_time(self):
        now_timestamp = datetime.now(tz=get_current_timezone())
        self.data['timestamp'] = now_timestamp

    def save(self):
        self.data.pop('country_name')
        print self.data
        attack = Attack(**self.data)
        attack.save()
        return attack