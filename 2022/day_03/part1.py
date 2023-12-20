def get_value(line):
    length = int(len(line) / 2)
    first = line[:length]
    second = line[length:]
    # Find the common part.
    for i in list(first):
        for j in list(second):
            if i == j:
                common = i
                break

    if common.isupper():
        score = ord(common) - 38
    else:
        score = ord(common) - 96

    return score



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    return sum([get_value(line) for line in lines])


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 157


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
