from json import loads
from http.client import HTTPSConnection
from collections import namedtuple
from collections import OrderedDict


class DataProvider:
    @staticmethod
    def get_new_cases_day(countries):
        # request cases from API, limits to 200 countries, may need to be increased in certain cases
        client = HTTPSConnection("api.coronatracker.com")
        client.request("GET", "/v3/analytics/dailyNewStats?limit=200", '', {})
        response = client.getresponse()
        response = response.read().decode("utf-8")
        client.close()

        # transform response to list, API responds with ordered list by case numbers
        parsed_json = loads(response, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        top_five = []
        for i in range(0, 5 - len(countries)):
            top_five.append((parsed_json[i].country, parsed_json[i].daily_cases))

        # always include requested countries, otherwise use top 5 in # of cases
        counter = 0
        for country in countries:
            if counter == 5:
                break
            obj = {obj for obj in parsed_json if obj.country == country}.pop()
            top_five.append((obj.country, obj.daily_cases))
            counter += 1

        # sort before returning
        return sorted(top_five, reverse=True, key=lambda tup: tup[1])
