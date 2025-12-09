from collections import defaultdict
from tqdm import tqdm

import utils

filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().splitlines()
list_pos = [tuple(int(p) for p in line.split(",")) for line in lines]

max_area = 0
for i in range(len(list_pos)):
    for j in range(len(list_pos)):
        if i == j:
            continue

        abs_x = abs(list_pos[i][0] - list_pos[j][0]) + 1
        abs_y = abs(list_pos[i][1] - list_pos[j][1]) + 1
        area = abs_x * abs_y
        if area > max_area:
            max_area = area

print("Part 1:", max_area)


# Part 2 is a totally different beast. Let's first turn into dictionary.
max_x = max([pos[0] for pos in list_pos])
max_y = max([pos[1] for pos in list_pos])
dict_board = {
    (i, j): "." for i in range(max_x + 1) for j in range(max_y + 1)
}
for pos in list_pos:
    # R is for Red
    dict_board[pos] = "R"


# utils.viz_board(dict_board)
# print("")

print("Filling in X positions...")
# Find x positions that have at least 2 occurrences.
dict_x_count = defaultdict(int)
for pos in list_pos:
    dict_x_count[pos[0]] += 1

list_x = [x for x, count in dict_x_count.items() if count >= 2]
for x in list_x:
    # Get the min and max y.
    min_y = min([pos[1] for pos in list_pos if pos[0] == x])
    max_y = max([pos[1] for pos in list_pos if pos[0] == x])
    # Fill in the board with "G" from min_y to max_y.
    # G is for Green
    for y in range(min_y, max_y + 1):
        dict_board[(x, y)] = "G"

# utils.viz_board(dict_board)
# print("")

print("Filling in Y positions...")
# Find the Y positions that have at least 2 occurrences.
dict_y_count = defaultdict(int)
for pos in list_pos:
    dict_y_count[pos[1]] += 1
list_y = [y for y, count in dict_y_count.items() if count >= 2]
for y in list_y:
    # Get the min and max x.
    min_x = min([pos[0] for pos in list_pos if pos[1] == y])
    max_x = max([pos[0] for pos in list_pos if pos[1] == y])
    # Fill in the board.
    for x in range(min_x, max_x + 1):
        dict_board[(x, y)] = "G"


# utils.viz_board(dict_board)
# print("")

print("Finding inside positions...")
inside_pos = utils.find_inside_positions(dict_board=dict_board, boundary_char="G")

for pos in inside_pos:
    dict_board[pos] = "i"

# utils.viz_board(dict_board)
# print("")

eligible_pos = set([pos for pos in dict_board.keys() if dict_board[pos] != "."])

# Then we check every pairwise combination.
# Warning it might be slow!

def get_area(pos1, pos2):
    x_min = min(pos1[0], pos2[0])
    x_max = max(pos1[0], pos2[0])
    y_min = min(pos1[1], pos2[1])
    y_max = max(pos1[1], pos2[1])
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            if (x, y) not in eligible_pos:
                return 0

    return (x_max - x_min + 1) * (y_max - y_min + 1)


max_area = 0
for i in tqdm(range(len(list_pos))):
    for j in tqdm(range(len(list_pos))):
        if i == j:
            continue

        pos1 = list_pos[i]
        pos2 = list_pos[j]
        area = get_area(pos1, pos2)
        if area > max_area:
            max_area = area


print("Part 2:", max_area)
