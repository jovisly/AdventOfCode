def solve(filename):
    lines = open(filename, encoding="utf-8").read().split("\n\n")
    lines = [line.splitlines() for line in lines]

    sums = sorted([sum([int(a) for a in arr]) for arr in lines], reverse=True)
    return sum(sums[:3])


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 45000


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
