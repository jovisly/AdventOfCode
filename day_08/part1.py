
def get_dict_instructions(lines):
    dict_instructions = {}
    for line in lines:
        key = line[:3]
        l = line[7:10]
        r = line[12:15]
        dict_instructions[key] = {"L": l, "R": r}
    return dict_instructions


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    dict_instructions = get_dict_instructions(lines[2:])
    steps = list(lines[0])

    node = "AAA"
    num_steps = 0
    while node != "ZZZ":
        ind_steps = num_steps % len(steps)
        step = steps[ind_steps]
        node = dict_instructions[node][step]
        num_steps += 1

    return num_steps


def mini_test():
    filename = "input-test1.txt"
    assert solve(filename) == 2

    filename = "input-test2.txt"
    assert solve(filename) == 6


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    output = solve(filename)

    print(output)

