MARKER_LENGTH = 4


def find_marker(line, marker_length=MARKER_LENGTH):
    for ind in range(len(line)):
        if ind < marker_length:
            continue

        marker = line[ind - marker_length:ind]
        if len(set(list(marker))) == marker_length:
            return ind

    print("WARNING: NO MARKER FOUND")
    return -1



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    return find_marker(lines[0])


def mini_test():
    assert solve("input-test.txt") == 7
    assert solve("input-test2.txt") == 5
    assert solve("input-test3.txt") == 6
    assert solve("input-test4.txt") == 10
    assert solve("input-test5.txt") == 11



if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
