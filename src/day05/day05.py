import time

from src.utils import Inputstr, letters


# My original solution. Pretty simple (and maybe a bit naive), but it runs relatively slow (~200ms on the real input)
# compared to a solution using stacks
def original_part_1(inputs, cs):
    done = False
    new_string = inputs

    while not done:
        done = True
        for pair in cs:
            new_string = new_string.replace(pair, "")
        for pair in cs:
            if pair in new_string:
                done = False
                break
    return new_string


# I improved my part one after seeing examples of using stacks. Adapted it to my original part1
def part_1(input_string, cs):
    total_stack = []
    for c in input_string:
        total_stack.pop() if total_stack and total_stack[-1] + c in cs else total_stack.append(c)
    return "".join(total_stack)


def part_2(inputs, cs):
    info = []
    input_bab = inputs
    for letter in letters:
        new_string = input_bab.replace(letter.upper(), "").replace(letter.lower(), "")
        info.append((part_1(new_string, cs)))
    return min(info, key=len)


def create_containing_set():
    containing_set = set()
    for letter in letters:
        containing_set.add(letter.upper() + letter.lower())
        containing_set.add(letter.lower() + letter.upper())
    return containing_set


def get_input():
    return Inputstr("05", test=False)


def main():
    start_time_total = time.clock()
    input = get_input()

    start_time_part_1 = time.clock()

    containing_set = create_containing_set()
    tot_string = part_1(input, containing_set)
    end_time_part_1 = time.clock()
    print("Part 1 string: {}".format(tot_string))
    print("Part 1 length: {}".format(len(tot_string)))
    print("Part 1 time: {0:.2f}ms".format((end_time_part_1 - start_time_part_1) * 1000))

    start_time_part_2 = time.clock()
    most_efficient = part_2(input, containing_set)
    end_time_part_2 = time.clock()
    print("\nPart 2:", len(most_efficient))
    print("Part 2 time: {0:.2f}ms".format((end_time_part_2 - start_time_part_2) * 1000))

    print("\nTotal time day 5: {0:.2f}ms".format((time.clock() - start_time_total) * 1000))


if __name__ == "__main__":
    main()
