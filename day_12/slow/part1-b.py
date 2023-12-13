"""This one is faster than part1-a.py but still too slow for part 2.

It tries all the possible locations to place . in the string.
"""
import itertools
from tqdm import tqdm


def get_patterns_and_numbers(line):
    [pattern, numbers] = line.split(" ")
    numbers = [int(n) for n in numbers.split(",")]
    return pattern, numbers


def make_template_arr(numbers):
    """Given [2, 3], return ["", "##", ".", "###", ""].

    Then we can add more "." to construct the full sequence.
    """
    template_arr = [""]
    for index, number in enumerate(numbers):
        template_arr.append("#" * number)
        if index != len(numbers) - 1:
            template_arr.append(".")

    template_arr.append("")
    return template_arr


def get_all_possible_patterns(pattern, template_arr):
    # Number of dots we still need to allocate.
    num_dots = len(pattern) - len("".join(template_arr))
    # print("num_dots", num_dots)
    # Positions where the dots can go.
    positions = [i for i, chars in enumerate(template_arr) if "#" not in chars]
    # print("positions", positions)

    possibilities = itertools.combinations_with_replacement(positions, num_dots)
    num_valid = 0
    for possibility in possibilities:
        this_pattern = list(template_arr)
        for dot in possibility:
            this_pattern[dot] += "."

        # Check if the pattern is valid.
        this_pattern = "".join(this_pattern)
        if all([c1==c2 or c1=="?" for c1, c2 in zip(pattern, this_pattern)]):
            num_valid += 1

    return num_valid




def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    total = 0
    for line in tqdm(lines):
        pattern, numbers = get_patterns_and_numbers(line)
        template_arr = make_template_arr(numbers)
        total += get_all_possible_patterns(pattern, template_arr)

    return total


def mini_test():
    filename = "../input-test.txt"
    # 1, 4, 1, 1, 4, 10
    assert solve(filename) == 21


if __name__ == "__main__":
    mini_test()

    filename = "../input.txt"
    total = solve(filename)

    print(total)
