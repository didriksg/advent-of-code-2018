import time

import numpy as np

from src.utils import Inputstr


def part_1(tot_map, lines, total_size):
    for i, line in enumerate(lines):
        start, measure = line
        x, y = [int(n.replace(":", "")) for n in start.split(',')]
        xd, yd = [int(j) for j in measure.split("x")]
        total_size[i] = xd * yd

        for o in range(yd):
            current_row = tot_map[y + o][x:x + xd]
            for w, point in enumerate(current_row):
                if point != 0:
                    tot_map[y + o][x + w] = -1  # The area is overlapping
                else:
                    tot_map[y + o][x + w] = i  # Nothing occupying this area. Fill it with current id

    return np.unique(tot_map, return_counts=True)


def part_2(tot, uni, cnt):
    for i, j in enumerate(uni):
        j = int(j)
        if tot[j] == cnt[i]:  # If the total area a id occupies is the same as the given area, we've found our match
            return j + 1


def main():
    raw_lines = Inputstr("03").split("\n")
    line_info = [line.split(" ")[2:] for line in raw_lines]

    area_size = 1000
    total_map = np.zeros((area_size, area_size))
    total_size = [0] * (len(line_info) + 1)

    part_1_start = time.time()
    unique, counts = part_1(total_map, line_info, total_size)
    index = np.where(unique == -1)
    print("Part 1:", counts[index][0])
    print("Part 1 time:", (time.time() - part_1_start) * 1000)

    part_2_start = time.time()
    non_overlap_id = part_2(total_size, unique[2:], counts[2:])
    print("\nPart 2:", non_overlap_id)
    print("Part 2 time:", (time.time() - part_2_start) * 1000)

    print("Total time:", (time.time() - part_1_start) * 1000)


if __name__ == "__main__":
    main()
