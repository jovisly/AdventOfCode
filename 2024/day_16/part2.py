"""
Reflections: Pruning fest...
"""
from functools import cache, lru_cache
from tqdm import tqdm
from collections import defaultdict

import heapq
import random
import utils

filename = "input.txt"
min_points = 127520
# filename = "input-test.txt"
# min_points = 7036
lines = open(filename, encoding="utf-8").read().splitlines()

dict_board = utils.get_dict_board(lines)

start_pos = [p for p, v in dict_board.items() if v == "S"][0]
end_pos = [p for p, v in dict_board.items() if v == "E"][0]

@cache
def pos_dir_to_str(pos, dir):
    return f"{pos[0]},{pos[1]},{dir}"

@cache
def str_to_pos_dir(s):
    x, y, dir = s.split(",")
    return (int(x), int(y)), dir

@lru_cache(maxsize=10000)
def get_visited_from_path(path_str):
    visited_pos = set()
    for segment in path_str.split(":"):
        pos, _ = str_to_pos_dir(segment)
        visited_pos.add(pos)
    return frozenset(visited_pos)

dir = "R"
start_str = pos_dir_to_str(start_pos, dir)
queue = [(0, start_str)]
all_paths = []

last_points_seen = 0
paths_checked = 0
min_points_to_pos_dir = defaultdict(lambda: float('inf'))

@cache
def dist_to_end(pos):
    return abs(pos[0] - end_pos[0]) + abs(pos[1] - end_pos[1])

while queue:
    points, path_str = heapq.heappop(queue)
    paths_checked += 1

    # Sanity log.
    if points != last_points_seen and points % 100 == 0:
        print(f"Checking paths with {points} points... (checked {paths_checked} paths so far)")
        last_points_seen = points

    #######
    # Pruning
    #######
    # 1. Prune if we've already exceeded min_points.
    if points > min_points:
        continue

    last_segment = path_str.split(":")[-1]
    pos, dir = str_to_pos_dir(last_segment)

    # 2. Prune if we've reached this position with fewer points before.
    if points > min_points_to_pos_dir[(pos, dir)]:
        continue

    min_points_to_pos_dir[(pos, dir)] = min(points, min_points_to_pos_dir[(pos, dir)])

    # 3. Prune if we can't possibly reach the end in the remaining points. With some
    # buffer.
    if points + dist_to_end(pos) > min_points + 64:
        continue

    if pos == end_pos:
        if points == min_points:
            all_paths.append(path_str)
            print(f"Found a solution! Total solutions so far: {len(all_paths)}")
            continue

    # Only add new paths if we haven't exceeded min_points and do not return to the
    # same position already visited in the path.
    visited_pos = get_visited_from_path(path_str)
    new_pos = utils.move_to_dir(pos, dir)
    if new_pos in dict_board and dict_board[new_pos] != "#" and new_pos not in visited_pos:
        new_path = f"{path_str}:{pos_dir_to_str(new_pos, dir)}"
        if points + 1 <= min_points:
            heapq.heappush(queue, (points + 1, new_path))

    right_dir = utils.turn(dir, "R")
    left_dir = utils.turn(dir, "L")
    right_path = f"{path_str}:{pos_dir_to_str(pos, right_dir)}"
    left_path = f"{path_str}:{pos_dir_to_str(pos, left_dir)}"
    if points + 1000 <= min_points:
        heapq.heappush(queue, (points + 1000, right_path))
        heapq.heappush(queue, (points + 1000, left_path))


def viz_board(dict_board, os):
    max_x = max([p[0] for p in dict_board.keys()])
    max_y = max([p[1] for p in dict_board.keys()])
    for i in range(max_x + 1):
        full_line = ""
        for j in range(max_y + 1):
            if (i, j) in os:
                full_line += "O"
            else:
                full_line += dict_board[(i, j)]
        print(full_line)


print(f"Found {len(all_paths)} different paths with {min_points} points")

os = set()
for path_str in all_paths:
    for segment in path_str.split(":"):
        pos, _ = str_to_pos_dir(segment)
        os.add(pos)

# viz_board(dict_board, os)
print(len(os))
