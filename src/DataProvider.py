import json
import http.client
from collections import namedtuple


class DataProvider:
    def __init__(self):
        self.client = http.client.HTTPSConnection("api.coronatracker.com")
        self.payload = ''
        self.headers = {}

    def get_new_cases_day(self, country_code):
        self.client.request("GET", "/v3/analytics/dailyNewStats?limit=200", self.payload, self.headers)
        response = self.client.getresponse()
        response = response.read().decode("utf-8")
        parsed_json = json.loads(response, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

        result = [x for x in parsed_json if x.country_code == country_code]
        return result[0].daily_cases
