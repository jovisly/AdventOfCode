import ast
from functools import cmp_to_key

from part1 import compare


def compare_to_int(a, b):
    result = compare(a, b)
    # Again the tying really tripped me up.
    if result is None:
        return 0

    return 1 if result else -1


def solve(filename):
    lines = open(filename, encoding="utf-8").read().split("\n\n")
    lines = [l.splitlines() for l in lines]
    lines = [[ast.literal_eval(a) for a in l] for l in lines]

    all_components = [[[2]], [[6]]]
    for pair in lines:
        all_components += pair

    all_components = sorted(all_components, key=cmp_to_key(compare_to_int), reverse=True)
    ind1 = all_components.index([[2]]) + 1
    ind2 = all_components.index([[6]]) + 1

    return ind1 * ind2


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 140


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
