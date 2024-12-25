"""
Reflections: This. Took. Forever.

The idea is to (a) figure out the most optimal transition for every pair of keys.
We do this by trying out a couple of generations and hope there are no ties. In fact
there was a tie and I manually fixed the wrong one (by recognizing the fact that the
less we move on the keypad, the better).

Then (b) use the transition pairs to keep propagating the transitions. This works
well enough but SO. MANY. BUGS.
"""
import random
from tqdm import tqdm
import utils
import utils_d21
from collections import defaultdict

filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

n_remotes = 25
# n_remotes = 2


def get_shortest_path_length(goal):
    # Key: (curr_location, transition)
    dict_pairs = defaultdict(int)

    # Paths for keypad.
    path = "A" + utils_d21.get_shortest_paths_for_goal_keypad_only_one("A" + goal)
    # print("PATH:", path)
    for i in range(len(path) - 1):
        start = path[i]
        end = path[i + 1]
        dict_pairs[start + end] += 1

    # print("dict_pairs 1:", dict_pairs)
    # From now on we operate on the dictionary.
    for _ in range(n_remotes):
        new_dict_pairs = defaultdict(int)
        for k, v in dict_pairs.items():
            # Each k also evolves.
            path = "A" + utils_d21.get_shortest_paths_for_goal_remote_only_one(k)
            for i in range(len(path) - 1):
                start = path[i]
                end = path[i + 1]
                new_dict_pairs[start + end] += v

        dict_pairs = {k: v for k, v in new_dict_pairs.items()}

    # print("dict_pairs 2:", dict_pairs)
    return sum(dict_pairs.values())



tot = 0
for goal in tqdm(lines):
    p = get_shortest_path_length(goal)
    # print("GOAL:", goal, "PATH LENGTH:", p)
    tot += p * int(goal[:-1])


print("Part 2:", tot)

