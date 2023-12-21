import math

def get_stacks(line):
    lines = line.split("\n")
    num_stacks = int(lines[-1].strip().split("   ")[-1])

    raw_stacks = lines[:-1]
    raw_stacks = [
        stack.replace("[", " ").replace("]", " ") for stack in raw_stacks
    ]

    dict_stack = {
        i + 1: []
        for i in range(num_stacks)
    }

    for stack in raw_stacks:
        for i, char in enumerate(list(stack)):
            if char != " ":
                j = math.floor(i / 4) + 1
                dict_stack[j].append(char)

    return dict_stack


def update_stack(dict_stack, instruction, reverse=True):
    num_to_move = int(instruction.split(" ")[1])
    source = int(instruction.split(" ")[3])
    dest = int(instruction.split(" ")[5])

    arr_to_move = dict_stack[source][:num_to_move]
    if reverse == True:
        arr_to_move.reverse()
    dict_stack[source] = dict_stack[source][num_to_move:]
    dict_stack[dest] = arr_to_move + dict_stack[dest]
    return dict_stack


def solve(filename):
    lines = open(filename, encoding="utf-8").read().split("\n\n")

    instructions = lines[1].strip().split("\n")

    dict_stack = get_stacks(lines[0])
    for instruction in instructions:
        dict_stack = update_stack(dict_stack, instruction)

    return "".join([
        stack[0]
        for stack in dict_stack.values()
    ])


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == "CMZ"


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
