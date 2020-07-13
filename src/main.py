import time
from numpy import array_equal
from DataProvider import DataProvider
from InkyDriver import InkyDriver


def main():
    inky = InkyDriver()
    last_cycle = []
    countries = ["Germany"]  # maximum is 5

    start_time = time.time()
    while True:
        try:
            new_cases = DataProvider.get_new_cases_day(countries)
        except Exception as exception:
            exception = "Unexpected error of type" + str(type(exception)) + ":" + str(exception)
            print(exception)
            with open("log.txt", "a+") as f:
                f.write(str(exception))
            new_cases = []

        # only print if numbers changed
        cases = [cases[1] for cases in new_cases]
        if not array_equal(cases, last_cycle):
            inky.create_new_image(new_cases)

        last_cycle = cases
        # sleep 2 minutes
        time.sleep(120.0 - ((time.time() - start_time) % 120.0))
    

if __name__ == '__main__':
    main()
