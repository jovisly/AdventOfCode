"""
Time: ...

Reflections: ...

Bug report: ...
"""
import utils

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

max_depth = len(lines)
curr_pos = (0, 0)

dict_board = utils.get_dict_board(lines)

num_trees = 0
while True:
    # Check if we have a tree.
    x, y = curr_pos
    y = y % len(lines[0])
    val = dict_board[(x, y)]
    if val == "#":
        num_trees += 1

    # Move.
    y += 3
    x += 1
    if x == max_depth:
        break
    else:
        curr_pos = (x, y)


print("Part 1:", num_trees)


def check_by_move(dx, dy):
    curr_pos = (0, 0)
    num_trees = 0
    while True:
        # Check if we have a tree.
        x, y = curr_pos
        y = y % len(lines[0])
        val = dict_board[(x, y)]
        if val == "#":
            num_trees += 1

        # Move.
        y += dy
        x += dx
        # Need to switch this from == to >= when we increment x by more than 1.
        if x >= max_depth:
            break
        else:
            curr_pos = (x, y)
    return num_trees


a = check_by_move(1, 1)
b = check_by_move(1, 3)
c = check_by_move(1, 5)
d = check_by_move(1, 7)
e = check_by_move(2, 1)
print("Part 2:", a*b*c*d*e)
