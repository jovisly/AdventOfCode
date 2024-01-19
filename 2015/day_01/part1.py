def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()[0]
    return lines.count("(") - lines.count(")")


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == -3


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
