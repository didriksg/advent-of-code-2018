from src.utils import Inputstr
import time


def part_1(input):
    pass


def part_2(input):
    pass


def main():
    start_time_total = time.clock()
    input = None

    start_time_part_1 = time.clock()
    part_1(input)
    end_time_part_1 = time.clock()
    print("Part 1 time: {0:.2f}ms".format((end_time_part_1 - start_time_part_1) * 1000))

    start_time_part_2 = time.clock()
    part_2(input)
    end_time_part_2 = time.clock()
    print("Part 2 time: {0:.2f}ms".format((end_time_part_2 - start_time_part_2) * 1000))

    print("Total time: {0:.2f}ms".format((time.clock() - start_time_total) * 1000))


if __name__ == "__main__":
    main()
