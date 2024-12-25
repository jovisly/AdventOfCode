"""
Most difficult problem of the year. Will there be a more difficult one? Gasp.
"""
from tqdm import tqdm
import utils
import utils_d21

filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

def get_shortest_path_length(goal):
    p1 = utils_d21.get_shortest_paths_for_goal_keypad("A" + goal)
    p2 = []
    # print("p1", p1)
    for p in p1:
        p2 += utils_d21.get_shortest_paths_for_goal_remote("A" + p)

    min_len_p2 = min([len(p) for p in p2])
    p2 = set([p for p in p2 if len(p) == min_len_p2])
    # assert "v<<A>>^A<A>AvA<^AA>A<vAAA>^A" in p2

    p3 = []
    for p in p2:
        p3 += utils_d21.get_shortest_paths_for_goal_remote("A" + p)

    min_len_p3 = min([len(p) for p in p3])
    return min_len_p3

# goal = "029A"
# print(get_shortest_path_length(goal))
# exit()
tot = 0
for goal in tqdm(lines):
    tot += get_shortest_path_length(goal) * int(goal[:-1])

print("Part 1:", tot)
