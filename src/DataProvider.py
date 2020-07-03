import json
import http.client
from collections import namedtuple
from collections import OrderedDict


class DataProvider:
    @staticmethod
    def get_new_cases_day(countries):
        new_cases = {}
        client = http.client.HTTPSConnection("api.coronatracker.com")
        client.request("GET", "/v3/analytics/dailyNewStats?limit=200", '', {})
        response = client.getresponse()
        response = response.read().decode("utf-8")
        client.close()
        parsed_json = json.loads(response, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        for country_code in countries:
            result = [x for x in parsed_json if x.country_code == country_code]
            new_cases[countries[country_code]] = result[0].daily_cases

        # sort before returning
        return OrderedDict(sorted(new_cases.items(), reverse=True, key=lambda x: x[1]))
