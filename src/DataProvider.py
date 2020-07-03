import http.client
import mimetypes


class DataProvider:
    def __init__(self):
        self.client = http.client.HTTPSConnection("api.coronatracker.com")
        self.payload = ''
        self.headers = {}

    def get_new_cases_day(self, country_code=""):
        if len(country_code) == 0:
            self.client.request("GET", "/v3/analytics/dailyNewStats?limit=50", self.payload, self.headers)
        else:
            self.client.request("GET", f"/v3/analytics/newcases/country?countryCode={country_code}&startDate=2020-07-03&endDate=2020-07-04", self.payload, self.headers)
        response = self.client.getresponse()
        return response.read().decode("utf-8")
