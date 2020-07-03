import time
import numpy as np
from DataProvider import DataProvider
from InkyDriver import InkyDriver


def main():
    source = DataProvider()
    inky = InkyDriver()
    new_cases = []
    last_cycle = []
    countries = {
        "DE": "Germany",
        "US": "United States",
    }

    start_time = time.time()
    while True:
        print("tick")
        for key in countries.keys():
            new_cases.append(source.get_new_cases_day(key))

        # only print if numbers changed
        if not np.array_equal(new_cases, last_cycle):
            inky.create_new_image(countries, new_cases)

        last_cycle = new_cases
        # sleep 2 minutes
        time.sleep(120.0 - ((time.time() - start_time) % 120.0))


if __name__ == '__main__':
    main()
