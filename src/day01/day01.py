from itertools import cycle

from src.utils import Inputstr


def part_2(nums):
    freqs = {0}
    total = 0

    for number in cycle(nums):
        total += number
        if total in freqs:
            return total
        freqs.add(total)


def main():
    # Input and parsing
    lines_input = Inputstr("01").split("\n")
    numbers = [int(number) for number in lines_input]

    # Part 1
    print("Part 1:")
    print("Sum:", sum(numbers))

    # Part 2
    print("\nPart 2:")
    print("Duplicate frequency:", part_2(numbers))


if __name__ == "__main__":
    main()
