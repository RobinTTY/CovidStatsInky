from DataProvider import DataProvider
from InkyDriver import InkyDriver

def main():
    source = DataProvider()
    inky = InkyDriver()
    new_cases = []
    countries = {
        "DE": "Germany",
        "US": "United States",
    }

    for key in countries.keys():
        new_cases.append(source.get_new_cases_day(key))

    inky.create_new_image(countries, new_cases)


if __name__ == '__main__':
    main()
