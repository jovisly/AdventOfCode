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


# Part 2: Use coordinate compression - only unique x/y values (248x248 grid)
# Collect all unique x and y values from positions
all_x_values = set()
all_y_values = set()

for pos in list_pos:
    all_x_values.add(pos[0])
    all_y_values.add(pos[1])

print("number of x values:", len(all_x_values))
print("number of y values:", len(all_y_values))

# Create compression maps - map unique values to 0..247
sorted_x = sorted(all_x_values)
sorted_y = sorted(all_y_values)
x_to_compressed = {x: i for i, x in enumerate(sorted_x)}
y_to_compressed = {y: i for i, y in enumerate(sorted_y)}
compressed_to_x = {i: x for i, x in enumerate(sorted_x)}
compressed_to_y = {i: y for i, y in enumerate(sorted_y)}

# Compress positions
compressed_pos = [(x_to_compressed[pos[0]], y_to_compressed[pos[1]]) for pos in list_pos]

# Now work in compressed space
compressed_max_x = len(sorted_x) - 1
compressed_max_y = len(sorted_y) - 1
dict_board = {
    (i, j): "." for i in range(compressed_max_x + 1) for j in range(compressed_max_y + 1)
}
for pos in compressed_pos:
    dict_board[pos] = "R"


# utils.viz_board(dict_board)
# print("")

print("Filling in X positions...")
# Find x positions that have at least 2 occurrences
dict_x_count = defaultdict(int)
for pos in list_pos:
    dict_x_count[pos[0]] += 1
list_x = [x for x, count in dict_x_count.items() if count >= 2]

for x in list_x:
    min_y = min([pos[1] for pos in list_pos if pos[0] == x])
    max_y = max([pos[1] for pos in list_pos if pos[0] == x])
    comp_x = x_to_compressed[x]
    # Fill all compressed y cells that fall within [min_y, max_y]
    for comp_y, orig_y in enumerate(sorted_y):
        if min_y <= orig_y <= max_y:
            dict_board[(comp_x, comp_y)] = "G"

print("Filling in Y positions...")
# Find y positions that have at least 2 occurrences
dict_y_count = defaultdict(int)
for pos in list_pos:
    dict_y_count[pos[1]] += 1
list_y = [y for y, count in dict_y_count.items() if count >= 2]

for y in list_y:
    min_x = min([pos[0] for pos in list_pos if pos[1] == y])
    max_x = max([pos[0] for pos in list_pos if pos[1] == y])
    comp_y = y_to_compressed[y]
    # Fill all compressed x cells that fall within [min_x, max_x]
    for comp_x, orig_x in enumerate(sorted_x):
        if min_x <= orig_x <= max_x:
            dict_board[(comp_x, comp_y)] = "G"


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
# Work in compressed space, but calculate area in original space

def get_area_compressed(comp_pos1, comp_pos2):
    """Check if rectangle is valid and return area in original coordinate space."""
    comp_x_min = min(comp_pos1[0], comp_pos2[0])
    comp_x_max = max(comp_pos1[0], comp_pos2[0])
    comp_y_min = min(comp_pos1[1], comp_pos2[1])
    comp_y_max = max(comp_pos1[1], comp_pos2[1])

    # Check if all positions in rectangle are eligible
    for comp_x in range(comp_x_min, comp_x_max + 1):
        for comp_y in range(comp_y_min, comp_y_max + 1):
            if (comp_x, comp_y) not in eligible_pos:
                return 0

    # Convert back to original coordinates for area calculation
    orig_x_min = compressed_to_x[comp_x_min]
    orig_x_max = compressed_to_x[comp_x_max]
    orig_y_min = compressed_to_y[comp_y_min]
    orig_y_max = compressed_to_y[comp_y_max]

    return (orig_x_max - orig_x_min + 1) * (orig_y_max - orig_y_min + 1)


max_area = 0
for i in tqdm(range(len(compressed_pos))):
    for j in tqdm(range(len(compressed_pos))):
        if i == j:
            continue

        comp_pos1 = compressed_pos[i]
        comp_pos2 = compressed_pos[j]
        area = get_area_compressed(comp_pos1, comp_pos2)
        if area > max_area:
            max_area = area


print("Part 2:", max_area)
