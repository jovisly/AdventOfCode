"""
Reflections: Having utils is nice.

Bug report: For part 2, forgot I was originally doing set() and was counting set size
as a way to see if stuck (instead of list length). Which hit infinite loop.

Didn't do anything smart for part 2 -- just tried all positions. Took about 2 min.
"""
from tqdm import tqdm

import utils

filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

board = utils.get_dict_board(lines)

# Find the start.
for pos, val in board.items():
    if val == "^":
        start = pos
        break

dir = "U"
curr_pos = start
visited = set()
visited.add(curr_pos)

while True:
    new_pos = utils.move_to_dir(curr_pos, dir)
    if new_pos not in board:
        break

    # We might have to turn if we hit something.
    this_val = board[new_pos]
    if this_val == "#":
        # Turn right.
        dir = utils.turn(dir, "R")
        # Note we do not move to new positiion because stuff is there.
    else:
        curr_pos = new_pos
        visited.add(curr_pos)


print("Part 1:", len(visited))


# Can we just try all positions that are currently "."???
positions = [pos for pos, val in board.items() if val == "."]

def do_we_get_stuck(position):
    # Let's see if we turn it into a "#" if stuff will get messed up.
    board_copy = {
        k: v for k, v in board.items()
    }
    board_copy[position] = "#"

    dir = "U"
    curr_pos = start
    visited = [curr_pos]

    while True:
        new_pos = utils.move_to_dir(curr_pos, dir)
        if new_pos not in board_copy:
            break

        # We might have to turn if we hit something.
        this_val = board_copy[new_pos]
        if this_val == "#":
            # Turn right.
            dir = utils.turn(dir, "R")
            # Note we do not move to new positiion because stuff is there.
        else:
            curr_pos = new_pos
            visited.append(curr_pos)

        # Hey if we have more visited than board size, we probably got stuck.
        if len(visited) > len(board_copy):
            return True

    return False

s = 0
for position in tqdm(positions):
    if do_we_get_stuck(position):
        s += 1

print("Part 2:", s)
