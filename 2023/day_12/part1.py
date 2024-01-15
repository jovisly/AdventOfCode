from functools import cache


def get_patterns_and_numbers(line):
    [pattern, numbers] = line.split(" ")
    numbers = tuple(int(n) for n in numbers.split(","))
    return pattern, numbers


@cache
def get_num_ways(pattern, numbers, num_hashes):

    if pattern == "":
        # We have reached the end. Check if the num_hashes we have is valid.
        if num_hashes > 0:
            if len(numbers) > 0 and len(numbers) == 1 and num_hashes == numbers[0]:
                return 1
            else:
                # Invalid pattern.
                return 0
        else:
            if len(numbers) == 0:
                return 1
            else:
                return 0

    num_ways = 0
    possible_chars = ["#", "."] if pattern[0] == "?" else [pattern[0]]
    for char in possible_chars:
        if char == "#":
            num_ways += get_num_ways(pattern[1:], numbers, num_hashes + 1)

        if char == ".":
            if num_hashes > 0:
                if len(numbers) > 0 and num_hashes == numbers[0]:
                    # Finished with the current contiguous group of hashes,
                    # so exclude that from numbers and reset num_hashes.
                    num_ways += get_num_ways(pattern[1:], numbers[1:], 0)
                else:
                    # Invalid configuration.
                    # return 0
                    continue
            else:
                num_ways += get_num_ways(pattern[1:], numbers, 0)

    return num_ways



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    total = 0
    for line in lines:
        pattern, numbers = get_patterns_and_numbers(line)
        total += get_num_ways(pattern, numbers, num_hashes=0)

    return total


def mini_test():
    filename = "input-test.txt"
    # 1, 4, 1, 1, 4, 10
    assert solve(filename) == 21


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
