def tilt(lines):
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            if val == "O" and y > 0:
                y_above = [i for i in range(y)]
                vals_above = [lines[yi][x] for yi in y_above]
                if all([v == "." for v in vals_above]):
                    y_new = 0
                else:
                    y_new = max([ind for ind, v in enumerate(vals_above) if v != "."]) + 1

                if y_new != y:
                    lines[y][x] = "."
                    lines[y_new][x] = "O"

    return lines



def score(lines):
    total = 0
    for y, line in enumerate(lines):
        row_num = len(lines) - y
        for val in line:
            if val == "O":
                total += row_num
    return total



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    lines = [list(l) for l in lines]

    tilted = tilt(lines)
    return score(tilted)



def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 136



if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
