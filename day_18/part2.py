"""
Test data set:     6_405_262 edges
Actual data set: 173_561_416 edges

Iteration is simply impossible. The paths also can't be reduced with gcd. So we
use math: https://en.wikipedia.org/wiki/Shoelace_formula

There are several options. Here we use the Trapezoid formula:
A_i = (x_{i+1} - x_i) * (y_{i+1} + y_i) / 2
"""
from part1 import map_dir


def get_pos(curr_pos, instruction):
    dir = map_dir(instruction[0])
    num_steps = int(instruction[1])
    next_pos = (curr_pos[0] + num_steps * dir[0], curr_pos[1] + num_steps * dir[1])
    return next_pos


def get_all_pos(lines):
    curr_pos = (0,0)
    all_pos = []
    for line in lines:
        curr_pos = get_pos(curr_pos, line)
        all_pos.append(curr_pos)

    # We should end up back at the origin.
    assert all_pos[-1] == (0,0)
    return all_pos


def process_line(line):
    components = line.split(" ")
    dir_int = int(components[2][-2])
    if dir_int == 0:
        dir = "R"
    elif dir_int == 1:
        dir = "D"
    elif dir_int == 2:
        dir = "L"
    elif dir_int == 3:
        dir = "U"
    else:
        raise ValueError(f"Unknown direction: {dir_int}")
    num_steps = int(components[2][2:-2], 16)
    return dir, num_steps



def get_area(lines):
    a = 0
    processed_lines = [process_line(line) for line in lines]
    all_pos = get_all_pos(processed_lines)
    num_steps = 0
    for i in range(len(lines)):
        j = (i + 1) % len(all_pos)
        this_pos = all_pos[i]
        next_pos = all_pos[j]

        # Confusingly our coordinate system is (y, x).
        a += 0.5 * (this_pos[1] - next_pos[1]) * (this_pos[0] + next_pos[0])
        # Our line has width of 1, so we need to count that too. But note our
        # coordinate system is counting the area of the line also.
        num_steps += processed_lines[i][1]

    return int(a) + int((num_steps + 2) / 2)



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    return get_area(lines)


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 952408144115


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
