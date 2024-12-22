"""
Most difficult problem of the year. Will there be a more difficult one? Gasp.
"""
from tqdm import tqdm
import utils
import utils_d21

filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().splitlines()
list_keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["#", "0", "A"]
]

list_remote = [
    ["#", "^", "A"],
    ["<", "v", ">"]
]


dict_keypad = utils.get_dict_board(list_keypad)
dict_remote = utils.get_dict_board(list_remote)

all_keypad_paths = utils_d21.get_all_shortest_paths(dict_keypad)
all_remote_paths = utils_d21.get_all_shortest_paths(dict_remote)


def get_shortest_path_length(goal):
    p1 = utils_d21.get_shortest_paths_for_goal("A" + goal, dict_keypad, all_keypad_paths)
    p2 = []
    for p in p1:
        p2 += utils_d21.get_shortest_paths_for_goal("A" + p, dict_remote, all_remote_paths)

    min_len_p2 = min([len(p) for p in p2])
    p2 = set([p for p in p2 if len(p) == min_len_p2])
    # assert "v<<A>>^A<A>AvA<^AA>A<vAAA>^A" in p2

    p3 = []
    for p in p2:
        p3 += utils_d21.get_shortest_paths_for_goal("A" + p, dict_remote, all_remote_paths)

    min_len_p3 = min([len(p) for p in p3])
    return min_len_p3

tot = 0
for goal in tqdm(lines):
    tot += get_shortest_path_length(goal) * int(goal[:-1])

print("Part 1:", tot)
