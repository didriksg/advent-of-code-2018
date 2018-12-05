import time

import numpy as np

from src.utils import Inputstr


def part_1(tot_map, lines, total_size):
    for i, line in enumerate(lines, start=1):
        start, measure = line
        x, y = [int(n.replace(":", "")) for n in start.split(',')]
        xd, yd = [int(j) for j in measure.split("x")]
        total_size[i] = xd * yd

        for o in range(yd):
            current_row = tot_map[y + o, x:x + xd]
            tot_map[y + o, x:x + xd] = [-1 if point != 0 else i for w, point in enumerate(current_row)]

    return np.unique(tot_map, return_counts=True)



def part_2(tot, uni, cnt):
    for i, j in enumerate(uni):
        if tot[j] == cnt[i]:
            return j


def main():
    # Inputs and setup
    start_inputs = time.clock()

    line_info = [line.split(" ")[2:] for line in Inputstr("03", test=False).split("\n")]
    area_size = 1000
    total_map = np.zeros((area_size, area_size))
    total_size = [0] * (len(line_info) + 1)
    print("Setup time: {0:.2f}ms".format((time.clock() - start_inputs) * 1000))

    # Part 1
    part_1_start = time.clock()  # Timing

    unique, counts = part_1(total_map, line_info, total_size)
    index, = np.where(unique == -1)
    print("\nPart 1:", counts[index][0])
    print("Time part 2: {0:.2f}ms".format((time.clock() - part_1_start) * 1000))

    # Part 2
    part_2_start = time.clock()  # Timing

    unique_int = [int(i) for i in unique]
    non_overlap_id = part_2(total_size, unique_int[2:], counts[2:])
    print("\nPart 2:", non_overlap_id)
    print("Time part 2: {0:.2f}ms".format((time.clock() - part_2_start) * 1000))


if __name__ == "__main__":
    start_time = time.clock()
    main()
    print("\nTotal time: {0:.2f}ms".format((time.clock() - start_time) * 1000))
