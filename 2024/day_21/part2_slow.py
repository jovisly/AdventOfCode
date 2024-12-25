"""
Cached everything but still too slow.
"""
import random
from tqdm import tqdm
import utils
import utils_d21

filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

n_remotes = 25
# n_remotes = 2

def get_shortest_path_length(goal):
    # Paths for keypad.
    paths = utils_d21.get_shortest_paths_for_goal_keypad("A" + goal)
    # assert "<A^A>^^AvvvA" in paths
    for _ in tqdm(range(n_remotes)):
        next_paths = []
        for p in paths:
            next_paths += utils_d21.get_shortest_paths_for_goal_remote("A" + p)

        min_len = min([len(p) for p in next_paths])
        next_paths = [p for p in next_paths if len(p) == min_len]
        paths = next_paths
        # assert "v<<A>>^A<A>AvA<^AA>A<vAAA>^A" or "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A" in paths

    min_len_final = min([len(p) for p in next_paths])
    return min_len_final


# o = get_shortest_path_length(goal="980A")
# print(o)
# exit()
tot = 0
for goal in lines:
    tot += get_shortest_path_length(goal) * int(goal[:-1])

print("Part 2:", tot)
