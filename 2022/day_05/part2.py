from part1 import get_stacks, update_stack

def solve(filename):
    lines = open(filename, encoding="utf-8").read().split("\n\n")

    instructions = lines[1].strip().split("\n")

    dict_stack = get_stacks(lines[0])
    for instruction in instructions:
        dict_stack = update_stack(dict_stack, instruction, reverse=False)

    return "".join([
        stack[0]
        for stack in dict_stack.values()
    ])


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == "MCD"


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
