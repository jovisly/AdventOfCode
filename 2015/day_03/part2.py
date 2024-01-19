import utils

def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    line = lines[0]

    pos1 = (0, 0)
    set_pos1 = {pos1}

    pos0 = (0, 0)
    set_pos0 = {pos0}

    for i, m in enumerate(line):
        if m == "^":
            dir = "U"
        elif m == "v":
            dir = "D"
        elif m == ">":
            dir = "R"
        elif m == "<":
            dir = "L"

        if i % 2 == 0:
            pos0 = utils.move_to_dir(pos0, dir)
            set_pos0.add(pos0)
        else:
            pos1 = utils.move_to_dir(pos1, dir)
            set_pos1.add(pos1)

    set_pos = set_pos0.union(set_pos1)
    return len(set_pos)



if __name__ == "__main__":

    filename = "input.txt"
    total = solve(filename)

    print(total)
