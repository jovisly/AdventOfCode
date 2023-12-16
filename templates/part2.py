def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    # Stuff here.
    return 0


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 0


if __name__ == "__main__":
    mini_test()

    # filename = "input.txt"
    # total = solve(filename)

    # print(total)
