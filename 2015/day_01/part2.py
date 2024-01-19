def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()[0]
    f = 0
    for i, c in enumerate(list(lines)):
        if c == "(":
            f += 1
        elif c == ")":
            f -= 1

        if f == -1:
            return i + 1

    return 0


if __name__ == "__main__":
    filename = "input.txt"
    total = solve(filename)

    print(total)
