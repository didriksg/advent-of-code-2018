from collections import Counter

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


def main():
    lines_input = Inputstr("02").split("\n")
    print("Part 1:")
    print(part_1(lines_input))
    print()
    print("Part 2:")
    print(part_2(lines_input))


if __name__ == "__main__":
    main()
