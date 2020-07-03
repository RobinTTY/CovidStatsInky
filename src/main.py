import json
from collections import namedtuple
from DataProvider import DataProvider

def main():
    source = DataProvider()
    new_cases = source.get_new_cases_day()
    decode_json(new_cases)
    print(new_cases)


def decode_json(raw_json):
    parsed_json = json.loads(raw_json, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    print(parsed_json[0].country_code)


if __name__ == '__main__':
    main()
