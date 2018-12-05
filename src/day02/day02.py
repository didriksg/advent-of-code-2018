from collections import Counter
import time
from src.utils import Inputstr


def part_1(lines):
    two = three = 0
    for line in lines:
        count_values = Counter(line).values()
        two += int(2 in count_values)
        three += int(3 in count_values)
    return two * three


def part_2(lines):
    for i, ba in enumerate(lines):
        if i == len(lines) - 1:
            return None
        for bb in lines[i + 1:]:
            dif = [i for i in range(len(ba)) if ba[i] != bb[i]]
            if len(dif) == 1:
                return ba.replace(ba[dif[0]], "")

def get_input():
    return Inputstr("02").split("\n")

def main():
    start_time_total = time.clock()
    inputs = get_input()

    start_time_part_1 = time.clock()
    part_1_res = part_1(inputs)
    end_time_part_1 = time.clock()
    print("Part 1: {}".format(part_1_res))
    print("Part 1 time: {0:.2f}ms".format((end_time_part_1 - start_time_part_1) * 1000))

    start_time_part_2 = time.clock()
    part_2_res = part_2(inputs)
    end_time_part_2 = time.clock()

    print("\nPart 2: {}".format(part_2_res))
    print("Part 2 time: {0:.2f}ms".format((end_time_part_2 - start_time_part_2) * 1000))
    print("\nTotal time day 2: {0:.2f}ms".format((end_time_part_2 - start_time_total) * 1000))


if __name__ == "__main__":
    main()
