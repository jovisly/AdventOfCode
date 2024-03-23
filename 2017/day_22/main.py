# Problem type:
# ~~~~~~~~~~~~ utils are nice! ~~~~~~~~~~~~
import utils

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

# Get center.
assert len(lines) % 2 == 1
c = int((len(lines) - 1) / 2)
center = (c, c)
# print(center)

dict_board = utils.get_dict_board(lines)
# print(dict_board)

curr_pos = center
curr_dir = "U"

num_infections = 0
for _ in range(10000):
    if curr_pos in dict_board:
        cell = dict_board[curr_pos]
    else:
        cell = "."

    if cell == "#":
        # infected. turn right.
        curr_dir = utils.turn(curr_dir, "R")
        dict_board[curr_pos] = "."
    else:
        # Not infected. turn left.
        curr_dir = utils.turn(curr_dir, "L")
        dict_board[curr_pos] = "#"
        num_infections += 1
    # Take one step.
    curr_pos = utils.move_to_dir(curr_pos, curr_dir)

print("Part 1:", num_infections)

# Part 2; reset.
dict_board = utils.get_dict_board(lines)
curr_pos = center
curr_dir = "U"

# States: "." (clean) -> "W" (weakened) -> "#" (infected) -> "F" (flagged) -> "."
from tqdm import tqdm
num_infections = 0
for _ in tqdm(range(10000000)):
    if curr_pos in dict_board:
        cell = dict_board[curr_pos]
    else:
        cell = "."

    if cell == ".":
        # Clean.
        curr_dir = utils.turn(curr_dir, "L")
        dict_board[curr_pos] = "W"
    elif cell == "W":
        # Weakened.
        dict_board[curr_pos] = "#"
        num_infections += 1
    elif cell == "#":
        # Infected
        curr_dir = utils.turn(curr_dir, "R")
        dict_board[curr_pos] = "F"
    else:
        # Flagged. Turn two rights which reverses direction.
        curr_dir = utils.turn(curr_dir, "R")
        curr_dir = utils.turn(curr_dir, "R")
        dict_board[curr_pos] = "."
    # Take one step.
    curr_pos = utils.move_to_dir(curr_pos, curr_dir)


print("Part 2:", num_infections)
