import itertools
from tqdm import tqdm

def get_patterns_and_numbers(line):
    [pattern, numbers] = line.split(" ")
    numbers = [int(n) for n in numbers.split(",")]
    # They are repeated 5 times, separated by a question mark (pattern).
    pattern = "?".join([pattern] * 5)
    numbers = numbers * 5
    return pattern, numbers


def get_numbers(pattern):
    chunks = pattern.split(".")
    chunks = [c for c in chunks if c]
    return [len(c) for c in chunks]


def count_num_ways(pattern, numbers):
    # First we replace the question marks with all possibilities.
    num_qs = pattern.count("?")
    combs = itertools.product('#.', repeat=num_qs)
    num_valid = 0
    for comb in combs:
        new_pattern = pattern
        for c in comb:
            # Replace the first ? with the current character.
            new_pattern = new_pattern.replace("?", c, 1)

        new_numbers = get_numbers(new_pattern)
        if len(new_numbers) == len(numbers) and all([a == b for a, b in zip(new_numbers, numbers)]):
            num_valid += 1

    return num_valid



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    total = 0
    for line in tqdm(lines):
        pattern, numbers = get_patterns_and_numbers(line)
        total += count_num_ways(pattern, numbers)
    return total


def mini_test():
    filename = "input-test.txt"
    # 1, 16384, 1, 16, 2500, 506250
    assert solve(filename) == 525152


if __name__ == "__main__":
    mini_test()

    # filename = "input.txt"
    # total = solve(filename)

    # print(total)
