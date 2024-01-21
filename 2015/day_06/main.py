from tqdm import tqdm

def parse_instruction(instruction):
    elements = instruction.split(" ")
    start_pos = elements[-3]
    start_pos = tuple([int(pos) for pos in start_pos.split(",")])

    end_pos = elements[-1]
    end_pos = tuple([int(pos) for pos in end_pos.split(",")])

    if instruction.startswith("turn on"):
        operation = "on"
    elif instruction.startswith("turn off"):
        operation = "off"
    else:
        operation = "toggle"
    return operation, start_pos, end_pos


def apply_instruction(dict_lights, instruction):
    operation, start_pos, end_pos = parse_instruction(instruction)
    x_min = min(start_pos[0], end_pos[0])
    x_max = max(start_pos[0], end_pos[0])
    y_min = min(start_pos[1], end_pos[1])
    y_max = max(start_pos[1], end_pos[1])
    for i in range(x_min, x_max+1):
        for j in range(y_min, y_max+1):
            if operation == "on":
                dict_lights[(i, j)] = 1
            elif operation == "off":
                dict_lights[(i, j)] = -1
            else:
                dict_lights[(i, j)] *= -1
    return dict_lights


def apply_instruction2(dict_lights, instruction):
    operation, start_pos, end_pos = parse_instruction(instruction)
    x_min = min(start_pos[0], end_pos[0])
    x_max = max(start_pos[0], end_pos[0])
    y_min = min(start_pos[1], end_pos[1])
    y_max = max(start_pos[1], end_pos[1])
    for i in range(x_min, x_max+1):
        for j in range(y_min, y_max+1):
            if operation == "on":
                dict_lights[(i, j)] += 1
            elif operation == "off":
                dict_lights[(i, j)] -= 1
                if dict_lights[(i, j)] < 0:
                    dict_lights[(i, j)] = 0
            else:
                dict_lights[(i, j)] += 2
    return dict_lights



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    # Set up dict of grids from 0 to 999
    dict_lights = {
        # -1 is off and 1 is on.
        (i, j): -1
        for i in range(0, 1000)
        for j in range(0, 1000)
    }

    for instruction in tqdm(lines):
        dict_lights = apply_instruction(dict_lights, instruction)

    lights = list(dict_lights.values())
    num_lights_on = len([light for light in lights if light == 1])
    print("Part 1:", num_lights_on)


    dict_lights = {
        (i, j): 0
        for i in range(0, 1000)
        for j in range(0, 1000)
    }
    for instruction in tqdm(lines):
        dict_lights = apply_instruction2(dict_lights, instruction)

    print("Part 2:", sum(dict_lights.values()))



if __name__ == "__main__":
    filename = "input.txt"
    solve(filename)


