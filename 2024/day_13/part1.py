"""
Reflections: Reminds me of 2015 Day 22.
"""
from tqdm import tqdm
import heapq

import utils

filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().split("\n\n")

# print(lines)
nt_a = 3
nt_b = 1


def process_config(line):
    lines = line.splitlines()
    button_a = lines[0]
    button_b = lines[1]
    prize = lines[2]

    button_a_x, button_a_y = button_a.split("X+")[1].split(", Y+")
    button_b_x, button_b_y = button_b.split("X+")[1].split(", Y+")
    prize_x, prize_y = prize.split("X=")[1].split(", Y=")

    return int(button_a_x), int(button_a_y), int(button_b_x), int(button_b_y), int(prize_x), int(prize_y)



def find_min_t(ax, ay, bx, by, px, py):
    x, y = 0, 0
    queue = [(0, x, y)]
    visited = {(x, y)}

    while len(queue) > 0:
        # print("queue", queue)
        curr_t, x, y = heapq.heappop(queue)
        # Exit conditions.
        if (x, y) == (px, py):
            return curr_t
        if x > px or y > py:
            continue

        # Now we can push either button A or button B.
        if (x + ax, y + ay) not in visited:
            heapq.heappush(queue, (curr_t + nt_a, x + ax, y + ay))
            visited.add((x + ax, y + ay))
        if (x + bx, y + by) not in visited:
            heapq.heappush(queue, (curr_t + nt_b, x + bx, y + by))
            visited.add((x + bx, y + by))


tot = 0
for line in tqdm(lines):
    ax, ay, bx, by, px, py = process_config(line)
    out = find_min_t(ax, ay, bx, by, px, py)
    if out is not None:
        tot += out


print("Part 1:", tot)
