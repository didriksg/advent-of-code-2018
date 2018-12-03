from collections import Counter

from src.utils import Inputstr


def part_1(lines):
    two = three = 0

    for line in lines:
        chars = list(line)
        count = Counter(chars)
        count_values = count.values()

        if 2 in count_values:
            two += 1
        if 3 in count_values:
            three += 1

    return two * three


# Get the index of difference between two strings.
def diff(a, b):
    return [i for i in range(len(a)) if a[i] != b[i]]


def part_2(lines):
    num_of_lines = len(lines)
    for i in range(num_of_lines):
        if i == num_of_lines - 1:
            print("No solution found")
            return None, None, None, None

        for j in range(i + 1, num_of_lines):
            sa = lines[i]
            sb = lines[j]
            dif = diff(sa, sb)

            if len(dif) == 1:
                dif, = dif
                res = sa.replace(sa[dif], "")
                return sa, sb, dif, res


def main():
    lines_input = Inputstr("02").split("\n")
    print("Part 1:")
    print(part_1(lines_input))
    print()
    print("Part 2:")
    str_a, str_b, dif_index, res = part_2(lines_input)
    print("String A:", str_a)
    print("String B:", str_b)
    print("Difference index:", dif_index)
    print("Result:", res)


if __name__ == "__main__":
    main()
