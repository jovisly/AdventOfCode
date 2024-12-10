"""
Bug report: Part 1 - I thought we are counting the number of unique paths but turns
out we are counting the number of unique end positions.

Which! Turns out to be what Part 2 wants so THAT WAS CONVENIENT.
"""
import utils

filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

board = utils.get_dict_board(lines)
# Convert to ints.
board = {k: int(v) for k, v in board.items()}

heads = [
    (i, j) for i, j in board.keys()
    if board[(i, j)] == 0
]

def search_paths(start, part2=False):
    curr_pos = start
    # Each path is a list of positions. So paths is a list of lists.
    paths = [[curr_pos]]
    seen_paths = set()
    pos_end = set()
    while len(paths) > 0:
        curr_path = paths.pop(0)
        curr_pos = curr_path[-1]
        curr_val = board[curr_pos]
        neighbors = utils.get_neighbors(curr_pos)
        for n in neighbors:
            if n in board and board[n] == curr_val + 1:
                if board[n] == 9:
                    # A path is completed.
                    completed_path = tuple(curr_path + [n])
                    seen_paths.add(completed_path)
                    pos_end.add(n)
                else:
                    # Ongoing path.
                    paths.append(curr_path + [n])

    if part2:
        return len(seen_paths)
    else:
        return len(pos_end)

tot = 0
for head in heads:
    tot += search_paths(head)

print("Part 1:", tot)



tot = 0
for head in heads:
    tot += search_paths(head, part2=True)

print("Part 2:", tot)
