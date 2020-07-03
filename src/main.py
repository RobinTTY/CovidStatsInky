import time
import numpy as np
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
    while True:
        print("tick")
        new_cases = DataProvider.get_new_cases_day(countries)

        # only print if numbers changed
        if not np.array_equal(new_cases, last_cycle):
            inky.create_new_image(new_cases)

        last_cycle = list(new_cases.values())
        # sleep 2 minutes
        time.sleep(120.0 - ((time.time() - start_time) % 120.0))


if __name__ == '__main__':
    main()
