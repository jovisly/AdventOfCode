from tqdm import tqdm
from part1 import get_num_ways

# 1 is equivalent to part 1.
PATTERN_REPETITION = 5


def get_patterns_and_numbers(line):
    [pattern, numbers] = line.split(" ")
    numbers = [int(n) for n in numbers.split(",")]
    pattern = "?".join([pattern] * PATTERN_REPETITION)
    numbers = tuple(numbers * PATTERN_REPETITION)
    return pattern, numbers



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    total = 0
    for line in tqdm(lines):
        pattern, numbers = get_patterns_and_numbers(line)
        total += get_num_ways(pattern, numbers, num_hashes=0)

    return total



def mini_test():
    filename = "input-test.txt"
    # 1, 16384, 1, 16, 2500, 506250
    assert solve(filename) == 525152


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
