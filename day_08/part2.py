import math

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

    nodes = [n for n in list(dict_instructions) if n.endswith("A")]
    num_steps = 0
    arr_periodicity = [[] for _ in range(len(nodes))]

    # Get a few samples to identify a sequence. Turns out it's pretty circular.
    while not all([len(arr) >= 2 for arr in arr_periodicity]):
        ind_steps = num_steps % len(steps)
        step = steps[ind_steps]
        nodes = [dict_instructions[n][step] for n in nodes]
        num_steps += 1
        for ind, n in enumerate(nodes):
            if n.endswith("Z"):
                arr_periodicity[ind].append(num_steps)


    multiples = (arr[0] for arr in arr_periodicity)

    return math.lcm(*multiples)


def mini_test():
    filename = "input-test3.txt"
    assert solve(filename) == 6


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    output = solve(filename)

    print(output)
