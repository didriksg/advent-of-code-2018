import datetime
import time

current_day = datetime.datetime.now().day


def divider():
    return "--------------------------------------------------------------------------------------------------------\n"


def run(is_test=False):
    for i in range(1, current_day + 1):
        print(divider(), "\tDay {}".format(i) + "\n")
        day = "day{:0>2d}".format(i)
        day = day + "_test" if is_test else day
        day_exec = day + ".main()"
        day_import = "from src.{} import {} as {}".format(day, day, day)

        try:
            exec(day_import)
            exec(day_exec)
        except ImportError:
            print("Not yet implemented")


def main():
    start_time = time.clock()
    run()
    print(divider())
    end_time = time.clock()
    print("Overall time for AoC 2018: {0:.2f}ms".format((end_time - start_time) * 1000))


if __name__ == "__main__":
    main()
