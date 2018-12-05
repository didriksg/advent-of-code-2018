from itertools import cycle

from src.utils import Inputstr
import time

def part_2(nums):
    freqs = {0}
    total = 0

    for number in cycle(nums):
        total += number
        if total in freqs:
            return total
        freqs.add(total)


def part_1(nums):
    return sum(nums)


def get_input():
    lines_input = Inputstr("01", test=False).split("\n")
    return [int(number) for number in lines_input]


def main():
    start_time_total = time.clock()
    inputs = get_input()

    start_time_part_1 = time.clock()

    # Part 1
    part_1_res = part_1(inputs)
    end_time_part_1 = time.clock()
    print("Part 1: {}".format(part_1_res))
    print("Part 1 time: {0:.2f}ms".format((end_time_part_1 - start_time_part_1) * 1000))

    # Part 2
    start_time_part_2 = time.clock()
    part_2_res = part_2(inputs)
    print("\nPart 2: {}".format(part_2_res))
    end_time_part_2 = time.clock()
    print("Part 2 time: {0:.2f}ms".format((end_time_part_2 - start_time_part_2) * 1000))
    print("\nTotal time day 1: {0:.2f}ms".format((end_time_part_2 - start_time_total) * 1000))


if __name__ == "__main__":
    main()
