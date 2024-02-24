"""
My initial approach was to search the entire space, prioritized by number of
steps and the -1 * of number of numbers collected. That turned out to be too
slow.

Then the second method was to only search for shortest distance between every
pair of numbers. In that case, we don't retrace steps, so we can restrict on
only visiting new positions, which made the search extremely fast. Then we just
try all permutations for the fastest.
"""
import heapq
from itertools import permutations

from tqdm import tqdm

import utils


filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

dict_board = utils.get_dict_board(lines)
start = None
nums = []
for k, v in dict_board.items():
    if v == "0":
        start = k
    if v not in ["0", "#", "."]:
        nums.append(v)

# Not deduping but it should be unique.
print("Numbers to visit:", nums)
len_nums = len(nums)
assert start is not None



def construct_path(path, start=start, dict_board=dict_board):
    # given path, return (a) curr_pos, (b) number of numbers visited.
    pos = start
    collected = set()
    for step in list(path):
        pos = utils.move_to_dir(pos, step)
        if dict_board[pos] in nums:
            collected.add(dict_board[pos])
    return pos, collected


# Find shortest path between two numbers.
def find_path(s, e, dict_board=dict_board):
    # print("s:", s, "e:", e)
    pos_s, pos_e = None, None
    for k, v in dict_board.items():
        if v == s:
            pos_s = k
        if v == e:
            pos_e = k

    queue = [(0, pos_s)]
    visited = {s}

    while len(queue) > 0:
        curr_cost, curr_pos = heapq.heappop(queue)
        # print("curr_cost", curr_cost, "curr_pos", curr_pos)

        if curr_pos == pos_e:
            return curr_cost

        list_next_pos = utils.get_neighbors(curr_pos)
        list_next_pos = [
            pos for pos in list_next_pos
            if pos in dict_board and dict_board[pos] != "#"
            and pos not in visited
        ]
        for next_pos in list_next_pos:
            heapq.heappush(queue, (curr_cost + 1, next_pos))
            visited.add(next_pos)

    raise ValueError(f"Could not find a path from {s} to {e}")


dict_dist = {}
all_nums = nums + ["0"]
for i in tqdm(all_nums):
    for j in all_nums:
        if i < j:
            dict_dist[(i, j)] = find_path(s=i, e=j)

print(dict_dist)

# Now we take permutations.
perms = list(permutations(all_nums, len(all_nums)))
perms = [p for p in perms if p[0] == "0"]
min_dist = 10**9
for p in perms:
    dist = 0
    for i in range(1, len(p)):
        p1 = p[i]
        p2 = p[i - 1]
        if p1 < p2:
            s = p1
            e = p2
        else:
            s = p2
            e = p1
        dist += dict_dist[(s, e)]
    #     print(" ", dict_dist[(s, e)])
    # print("p", p, "dist", dist)
    if dist < min_dist:
        min_dist = dist

print("Part1 - min dist:", min_dist)

# Part 2: add another 0.
perms = list(permutations(all_nums, len(all_nums)))
perms = [p for p in perms if p[0] == "0"]
min_dist = 10**9
for p in perms:
    dist = 0
    for i in range(1, len(p)):
        p1 = p[i]
        p2 = p[i - 1]
        if p1 < p2:
            s = p1
            e = p2
        else:
            s = p2
            e = p1
        dist += dict_dist[(s, e)]

    # Add also the distance to go back to zero.
    dist += dict_dist[("0", p[-1])]
    if dist < min_dist:
        min_dist = dist

print("Part2 - min dist:", min_dist)
