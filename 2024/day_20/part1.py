"""
Reflection: Tried many ways of implementing cheating rules but I think it's sorta
equivalent to breaking one wall at a time. So this is what was done.
"""
from tqdm import tqdm
import heapq
import utils

filename = "input.txt"
min_diff = 100
# filename = "input-test.txt"
# min_diff = 1
lines = open(filename, encoding="utf-8").read().splitlines()

dict_board = utils.get_dict_board(lines)
s = [pos for pos, val in dict_board.items() if val == "S"][0]
e = [pos for pos, val in dict_board.items() if val == "E"][0]


def get_fastest_path(wall_pos):
    """Get fastest path from start to end with this wall removed."""
    dict_board_copy = utils.get_dict_board(lines)
    if wall_pos is not None:
        dict_board_copy[wall_pos] = "."
    queue = [(0, s)]
    visited = set()
    visited.add(s)

    while len(queue) > 0:
        n, pos = heapq.heappop(queue)
        if pos == e:
            return n

        for neighbor in utils.get_neighbors(pos):
            if neighbor in dict_board_copy and neighbor not in visited and dict_board_copy[neighbor] != "#":
                heapq.heappush(queue, (n + 1, neighbor))
                visited.add(neighbor)

    return float('inf')


no_cheat_time = get_fastest_path(None)
print("no cheat time", no_cheat_time)

walls = [pos for pos, val in dict_board.items() if val == "#"]
n = 0
for wall in tqdm(walls):
    time_with_wall = get_fastest_path(wall)
    if time_with_wall <= no_cheat_time - min_diff:
        # print(wall, time_with_wall)
        n += 1

print(n)
