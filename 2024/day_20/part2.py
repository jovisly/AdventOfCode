"""
Reflection: Woah for the longest time I thought we can have at most 6 walls because
that was the example. But it's actually 20. I was stuck on that for.. a... very long
time.
"""
from tqdm import tqdm
import heapq
import utils

filename = "input.txt"
min_diff = 100
# filename = "input-test.txt"
# min_diff = 50

lines = open(filename, encoding="utf-8").read().splitlines()

dict_board = utils.get_dict_board(lines)
s = [pos for pos, val in dict_board.items() if val == "S"][0]
e = [pos for pos, val in dict_board.items() if val == "E"][0]
walls = [pos for pos, val in dict_board.items() if val == "#"]
non_walls = [pos for pos, val in dict_board.items() if val == "."]

def get_fastest_path():
    queue = [(0, s)]
    visited = set()
    visited.add(s)

    while len(queue) > 0:
        n, pos = heapq.heappop(queue)
        if pos == e:
            return n

        for neighbor in utils.get_neighbors(pos):
            if neighbor in dict_board and neighbor not in visited and dict_board[neighbor] != "#":
                heapq.heappush(queue, (n + 1, neighbor))
                visited.add(neighbor)

    return float('inf')


no_cheat_time = get_fastest_path()
print("no cheat time", no_cheat_time)
print("num walls", len(walls))
print("num non-walls", len(non_walls))

# Break the path into three parts:
# 1 - from s to point
# 2 - WALLS
# 3 - from any point to e


def get_distances_from_point(start_pos):
    """Get shortest distances from pos to any point on the map."""
    distances = {start_pos: 0}
    queue = [(0, start_pos)]

    while queue:
        dist, pos = heapq.heappop(queue)
        if dist > distances[pos]:
            continue

        for neighbor in utils.get_neighbors(pos):
            if neighbor in dict_board and dict_board[neighbor] != "#":
                new_dist = dist + 1
                if neighbor not in distances or new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(queue, (new_dist, neighbor))

    return distances


paths1 = get_distances_from_point(s)
paths2 = get_distances_from_point(e)

unique_paths = set()

for p1 in paths1:
    for p2 in paths2:
        # How many walls are there between p1 and p2 max.
        wall_dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        if wall_dist <= 20:
            total_time = paths1[p1] + wall_dist + paths2[p2]
            if total_time <= no_cheat_time - min_diff:
                unique_paths.add((p1[0], p1[1], p2[0], p2[1]))

print(len(unique_paths))
