def solve(filename):
    lines = open(filename, encoding="utf-8").read().split("\n\n")
    lines = [line.splitlines() for line in lines]

    sums = [sum([int(a) for a in arr]) for arr in lines]
    print("sums", sums)
    return max(sums)


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 24000


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
