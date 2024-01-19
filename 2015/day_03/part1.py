import utils

def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    line = lines[0]

    pos = (0, 0)
    set_pos = {pos}
    for m in line:
        if m == "^":
            dir = "U"
        elif m == "v":
            dir = "D"
        elif m == ">":
            dir = "R"
        elif m == "<":
            dir = "L"

        pos = utils.move_to_dir(pos, dir)
        set_pos.add(pos)

    return len(set_pos)


if __name__ == "__main__":
    filename = "input.txt"
    total = solve(filename)

    print(total)
