from ast import literal_eval

def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    tot_mem = 0
    tot_str = 0
    tot_repr = 0
    for line in lines:
        tot_str += len(line)
        tot_mem += len(literal_eval(line))
        encoded_line = '"' + line.replace('\\', '\\\\').replace('"', '\\"') + '"'
        tot_repr += len(encoded_line)

    print("Part 1:", tot_str - tot_mem)
    print("Part 2:", tot_repr - tot_str)


if __name__ == "__main__":
    filename = "input.txt"
    solve(filename)


