import time
from numpy import array_equal
from DataProvider import DataProvider
from InkyDriver import InkyDriver


def main():
    inky = InkyDriver()
    last_cycle = []
    countries = {
        "DE": "Germany",
        "US": "United States",
        "IN": "India",
        "BR": "Brazil",
    }

    start_time = time.time()
    try:
        while True:
            new_cases = DataProvider.get_new_cases_day(countries)

            # only print if numbers changed
            if not array_equal(new_cases.values(), last_cycle):
                inky.create_new_image(new_cases)

            last_cycle = list(new_cases.values())
            # sleep 2 minutes
            time.sleep(120.0 - ((time.time() - start_time) % 120.0))
    except Exception as exception:
        exception = "Unexpected error of type" + str(type(exception)) + ":" + str(exception)
        print(exception)
        with open("log.txt", "a+") as f:
            f.write(str(exception))


if __name__ == '__main__':
    main()
