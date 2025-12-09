from collections import defaultdict

import utils

filename = "input.txt"
filename = "input-test.txt"
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


utils.viz_board(dict_board)
print("")

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

utils.viz_board(dict_board)
print("")

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


utils.viz_board(dict_board)
print("")

# For every point, we want to see if it's "inside". That means it should find a G before AND after it.

def is_inside(dict_board, pos):
    if dict_board[pos] == "G":
        return False
    # if dict_board[pos] != "." and dict_board[pos] != "i":
    #     return True

    # Ray casting: cast rays in all four directions and count G borders.
    # If odd number of crossings in ALL directions, we're inside; otherwise outside.
    gs_left = len([
        p for p in list(dict_board.keys())
        if p[0] == pos[0] and p[1] < pos[1] and dict_board[p] == "G"
    ])
    gs_right = len([
        p for p in list(dict_board.keys())
        if p[0] == pos[0] and p[1] > pos[1] and dict_board[p] == "G"
    ])
    gs_up = len([
        p for p in list(dict_board.keys())
        if p[0] < pos[0] and p[1] == pos[1] and dict_board[p] == "G"
    ])
    gs_down = len([
        p for p in list(dict_board.keys())
        if p[0] > pos[0] and p[1] == pos[1] and dict_board[p] == "G"
    ])

    # print("?????")
    # print(gs_left, gs_right, gs_up, gs_down)

    # Inside if odd number of crossings in ALL directions
    return (gs_left % 2 == 1 and
            gs_right % 2 == 1 and
            gs_up % 2 == 1 and
            gs_down % 2 == 1)


# dict_board[(4, 4)] = "i"
# res = is_inside(dict_board, (3, 4))
# print(res)


for pos in list(dict_board.keys()):
    if is_inside(dict_board, pos):
        dict_board[pos] = "i"

utils.viz_board(dict_board)
print("")

print("Part 2:")
