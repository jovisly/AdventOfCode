def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    lines = [line.split("x") for line in lines]

    tot = 0
    for l in lines:
        l = sorted([int(x) for x in l])
        # Wrap.
        tot += 2 * (l[0] + l[1])
        # Bow.
        tot += l[0] * l[1] * l[2]

    return tot


if __name__ == "__main__":
    filename = "input.txt"
    total = solve(filename)

    print(total)
