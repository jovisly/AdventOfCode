# Problem type:
# ~~~~~~~~~~~~ very interesting! ~~~~~~~~~~~~
# Not as bad as the input data might look. It's very interesting how a visually
# easy task of tracing the line takes a lot of thought to code up properly.
import utils

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()
dict_board = utils.get_dict_board(lines)
# print(dict_board)

# Find starting point.
start = None
for i in range(len(lines[0])):
    if dict_board[(0, i)] == "|":
        start = (0, i)

assert start is not None

# Start traversing.
curr_pos = start
curr_dir = "D"
visited = {start}
letters = []
num_steps = 1
while True:
    # Move to next position.
    next_pos = utils.move_to_dir(curr_pos, curr_dir)
    if next_pos not in dict_board or dict_board[next_pos] == " ":
        break
    num_steps += 1
    # If next pos is "+" then we can change direction.
    next_dir = None
    if dict_board[next_pos] == "+":
        # Direction is whichever neighbor not already visited.
        next_dirs = []
        for dir in utils.DIRS4:
            n = utils.move_to_dir(next_pos, dir)
            if (
                n != curr_pos and n not in visited
                and n in dict_board and dict_board[n] != " "
            ):
                next_dirs.append(dir)

        assert len(next_dirs) == 1
        next_dir = next_dirs[0]
    else:
        next_dir = curr_dir

    if dict_board[next_pos] not in ["+", "|", "-"]:
        letters.append(dict_board[next_pos])


    curr_pos = next_pos
    visited.add(curr_pos)
    if next_dir is None:
        # Don't change next direction.
        pass
    else:
        curr_dir = next_dir




print("Part 1:", "".join(letters))
print("Part 2:", num_steps)
