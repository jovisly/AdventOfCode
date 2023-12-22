from part1 import find_marker

MARKER_LENGTH = 14


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    return find_marker(lines[0], marker_length=MARKER_LENGTH)



def mini_test():
    assert solve("input-test.txt") == 19
    assert solve("input-test2.txt") == 23
    assert solve("input-test3.txt") == 23
    assert solve("input-test4.txt") == 29
    assert solve("input-test5.txt") == 26


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
