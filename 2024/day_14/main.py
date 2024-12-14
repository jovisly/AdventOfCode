"""
Reflections: Tree tree tree!
"""
from tqdm import tqdm
import utils

filename = "input.txt"
w = 101
h = 103

# filename = "input-test.txt"
# w = 11
# h = 7

lines = open(filename, encoding="utf-8").read().splitlines()

# print(lines)

def get_robot(line):
    position, velocity = line.split(" v=")
    px, py = map(int, position.replace("p=", "").split(","))
    vx, vy = map(int, velocity.split(","))
    return px, py, vx, vy


def viz(pos):
    print("")
    for y in range(h):
        full_line = ""
        for x in range(w):
            if (x, y) == pos:
                full_line += "#"
            else:
                full_line += "."
        print(full_line)


dict_q = {
    "Top left": 0,
    "Bottom left": 0,
    "Top right": 0,
    "Bottom right": 0,
}

for line in tqdm(lines):
    # line = "p=2,4 v=2,-3"
    px, py, vx, vy = get_robot(line)
    # print(px, py, vx, vy)
    pos = (px, py)
    # viz(pos)
    for _ in range(100):
        new_x = (pos[0] + vx) % w
        new_y = (pos[1] + vy) % h
        pos = (new_x, new_y)
        # print(pos)
        # viz(pos)
    # Check which quardrant.
    print(pos)
    if pos[0] < w // 2 and pos[1] < h // 2:
        dict_q["Top left"] += 1
    elif pos[0] < w // 2 and pos[1] > h // 2:
        dict_q["Bottom left"] += 1
    elif pos[0] > w // 2 and pos[1] < h // 2:
        dict_q["Top right"] += 1
    elif pos[0] > w // 2 and pos[1] > h // 2:
        dict_q["Bottom right"] += 1


tot = 1
for v in dict_q.values():
    tot *= v

print("Part 1:", tot)

# LOL I GUESS WE DRAWING!


def get_board(w, h):
    return {(x, y): "." for x in range(w) for y in range(h)}


def viz_board(board):
    for y in range(h):
        full_line = ""
        for x in range(w):
            full_line += board[(x, y)]
        print(full_line)



import time

list_pos = []

for i in range(2000, 10000):
    print("********", i, "********")
    time.sleep(0.05)
    board = get_board(w, h)
    for line in lines:
        px, py, vx, vy = get_robot(line)
        pos = ((px + i * vx) % w, (py + i * vy) % h)
        board[pos] = "#"

    viz_board(board)
        # if i == 100:
        #     list_pos.append(pos)



    #     board[pos] = "#"

    # viz_board(board)
    # # Pause if user presses enter
# print(list_pos)
# dict_q = {
#     "Top left": 0,
#     "Bottom left": 0,
#     "Top right": 0,
#     "Bottom right": 0,
# }

# for pos in list_pos:
#     # Check which quardrant.
#     if pos[0] < w // 2 and pos[1] < h // 2:
#         dict_q["Top left"] += 1
#     elif pos[0] < w // 2 and pos[1] > h // 2:
#         dict_q["Bottom left"] += 1
#     elif pos[0] > w // 2 and pos[1] < h // 2:
#         dict_q["Top right"] += 1
#     elif pos[0] > w // 2 and pos[1] > h // 2:
#         dict_q["Bottom right"] += 1


# tot = 1
# for v in dict_q.values():
#     tot *= v

# print("Part 2:", tot)
