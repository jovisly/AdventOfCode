def is_fully_overlap(line):
    elements = line.split(",")
    elements = [e.split("-") for e in elements]
    elements = [[int(e[0]), int(e[1])] for e in elements]
    e0 = elements[0]
    e1 = elements[1]
    if e0[0] <= e1[0] and e0[1] >= e1[1]:
        return 1

    if e1[0] <= e0[0] and e1[1] >= e0[1]:
        return 1

    return 0



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    return sum([is_fully_overlap(line) for line in lines])


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 2


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
