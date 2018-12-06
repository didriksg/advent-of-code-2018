from src.utils import Inputstr
import time

import numpy as np

def part_1(input):
    max_x = max_y = 0
    x_y coords = set()
    for i in input:
        x, y = [int(i) for i in i.split(",")]
        max_x = max(max_x,x)
        max_y = max(max_y,y)

    map =

def part_2(input):
    pass


def get_input():
    return Inputstr("06", test=True).split("\n")


def main():
    start_time_total = time.clock()
    inputs = get_input()

    start_time_part_1 = time.clock()
    part_1_res = part_1(inputs)
    end_time_part_1 = time.clock()
    print("Part 1: {}".format(part_1_res))
    print("Part 1 time: {0:.2f}ms".format((end_time_part_1 - start_time_part_1) * 1000))

    # start_time_part_2 = time.clock()
    # part_2_res = part_2(inputs)
    # print("Part 2: {}".format(part_2_res))
    # end_time_part_2 = time.clock()
    # print("Part 2 time: {0:.2f}ms".format((end_time_part_2 - start_time_part_2) * 1000))
    #
    # print("Total time day X: {0:.2f}ms".format((time.clock() - start_time_total) * 1000))


if __name__ == "__main__":
    main()
