def get_value(lines):
    for i in list(lines[0]):
        for j in list(lines[1]):
            for k in list(lines[2]):
                if i == j and i == k:
                    common = i
                    break

    if common.isupper():
        score = ord(common) - 38
    else:
        score = ord(common) - 96

    return score



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    # Split the lines into groups of three.
    lines = [lines[i:i + 3] for i in range(0, len(lines), 3)]
    return sum([get_value(line) for line in lines])


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 70


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
