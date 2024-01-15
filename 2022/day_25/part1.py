"""
Time: 40 min.

Reflections: I like this question. Good to shift gears into math after several
path search / grid move problems.
"""
from functools import cache

import math

def get_int(s):
    if s == "-":
        return -1
    elif s == "=":
        return -2
    else:
        return int(s)


def get_str(n):
    if n == -1:
        return "-"
    elif n == -2:
        return "="
    else:
        return str(n)


def get_snafu_num(input_str):
    # Reverse the string.
    input_str = input_str[::-1]
    tot = 0
    for i, s in enumerate(input_str):
        base = math.pow(5, i)
        tot += base * get_int(s)
    return tot


@cache
def get_min_max_diff(p):
    # There should be no difference at 0.
    if p == 0:
        return (0, 0)
    # Some diff allowed.
    if p == 1:
        return (-2, 2)

    curr_min = -2 * math.pow(5, p - 1)
    curr_max = 2 * math.pow(5, p - 1)
    prev_min, prev_max = get_min_max_diff(p - 1)
    return (curr_min + prev_min, curr_max + prev_max)


def get_snafu_str(num):
    num_digits = math.floor(math.log(num, 5)) + 1
    remainder = num
    output = ""
    for i in range(num_digits):
        p = num_digits - i - 1
        b = math.pow(5, p)
        min_r, max_r = get_min_max_diff(p)

        for v in [2, 1, 0, -1, -2]:
            test_r = remainder - v * b
            if test_r >= min_r and test_r <= max_r:
                output += get_str(v)
                remainder = test_r
                break

    return output


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    tot = sum([get_snafu_num(line) for line in lines])
    print("Total:", tot)
    return get_snafu_str(tot)


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == "2=-1=0"


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
