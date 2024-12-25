"""
7 8 9
4 5 6
1 2 3
  0 A  bot1 (keypad)

  ^ A
< v >  bot2 (remote)

  ^ A
< v >  bot3 (remote)

  ^ A
< v >  you (remote)
"""
from tqdm import tqdm
from functools import cache
from collections import defaultdict
import heapq
import random
import utils

dirs = [">", "<", "^", "v"]

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
# print("dict_keypad", dict_keypad)
# print("dict_keypad")


@cache
def get_pos_keypad(value):
    return next((pos for pos, val in dict_keypad.items() if val == value), None)

@cache
def get_pos_remote(value):
    """Quick conversion to go from, e.g., A to (i, j)."""
    return next((pos for pos, val in dict_remote.items() if val == value), None)


def get_shortest_paths(start, end, dict_board):
    # dist, pos, path (moves)
    queue = [(0, start, "")]
    seen = defaultdict(lambda: float('inf'))
    seen[start] = 0
    paths = []

    while queue:
        dist, pos, path = heapq.heappop(queue)

        if dist > seen[pos]:
            continue

        if pos == end:
            if path:
                paths.append(''.join(path))
            continue

        for dir in dirs:
            next_pos = utils.move_to_dir(pos, dir)
            if next_pos not in dict_board or dict_board[next_pos] == "#":
                continue
            new_dist = dist + 1
            if new_dist <= seen[next_pos]:
                seen[next_pos] = new_dist
                heapq.heappush(queue, (new_dist, next_pos, path + dir))

    return paths if paths else []


def get_all_shortest_paths(dict_board):
    positions = list(dict_board.keys())
    all_paths = {}
    for start in positions:
        for end in positions:
            if start != end and (start, end) not in all_paths:
                paths = get_shortest_paths(start, end, dict_board)
                if paths:
                    all_paths[(start, end)] = paths

    return all_paths


# There are multiple paths between any two keys, but some are more efficient than
# others. We can determine efficiency by considering the distance we need to traverse.
def get_dist_path(path):
    # Each path starts with A and ends with A.
    full_path = "A" + path + "A"
    total_dist = 0
    for i in range(len(full_path) - 1):
        start = full_path[i]
        end = full_path[i + 1]
        start_pos = get_pos_remote(start)
        end_pos = get_pos_remote(end)
        dist = abs(start_pos[0] - end_pos[0]) + abs(start_pos[1] - end_pos[1])
        total_dist += dist
    return total_dist



all_keypad_paths = get_all_shortest_paths(dict_keypad)
all_remote_paths = get_all_shortest_paths(dict_remote)


@cache
def get_shortest_paths_for_goal_keypad(goal):
    # print("goal:", goal)
    result = [""]
    for i in range(len(goal) - 1):
        start = goal[i]
        end = goal[i + 1]
        start_pos = get_pos_keypad(start)
        end_pos = get_pos_keypad(end)
        # print("start:",start, start_pos, "end:", end, end_pos)
        if start_pos == end_pos:
            # Already there, then just press the button.
            result = [r + "A" for r in result]
        else:
            paths = all_keypad_paths[(start_pos, end_pos)]
            # Add the path to every path in result.
            new_result = []
            for r in result:
                for p in paths:
                    # Add the "A" for button press.
                    new_result.append(r + p + "A")
            result = new_result

    return [r for r in result if r]


@cache
def get_shortest_paths_for_goal_remote(goal):
    result = [""]
    for i in range(len(goal) - 1):
        start = goal[i]
        end = goal[i + 1]
        start_pos = get_pos_remote(start)
        end_pos = get_pos_remote(end)
        # print("start:",start, start_pos, "end:", end, end_pos)
        if start_pos == end_pos:
            # Already there, then just press the button.
            result = [r + "A" for r in result]
        else:
            paths = all_remote_paths[(start_pos, end_pos)]
            # Add the path to every path in result.
            new_result = []
            for r in result:
                for p in paths:
                    # Add the "A" for button press.
                    new_result.append(r + p + "A")
            result = new_result

    return [r for r in result if r]

# print(dict_keypad)
# We only need to do this once and we can remember it.
def get_most_optimal_path(goal):
    assert len(goal) == 2
    pos0 = get_pos_keypad(goal[0])
    pos1 = get_pos_keypad(goal[1])
    if pos0 == pos1:
        return "A"
    paths = all_keypad_paths[(pos0, pos1)]
    # print("paths:", paths)
    if len(paths) == 1:
        return paths[0] + "A"

    # Track total path lengths for each original path
    path_scores = defaultdict(list)

    for original_path in paths:
        current_paths = [original_path]

        # Simulate n_remotes generations -- increase until we dont get tying top paths.
        for gen in range(3):
            next_paths = []
            for p in current_paths:
                # Only add 'A' at the end, not beginning
                remote_paths = get_shortest_paths_for_goal_remote(p + "A")
                next_paths.extend(remote_paths)

            # Keep track of lengths for this generation
            min_len = min(len(p) for p in next_paths) if next_paths else 0
            path_scores[original_path].append(min_len)
            current_paths = [p for p in next_paths if len(p) == min_len]

    # Calculate total scores
    total_scores = {path: sum(scores) for path, scores in path_scores.items()}
    min_score = min(total_scores.values())

    # Find all paths with the minimum score
    best_paths = [path for path, score in total_scores.items() if score == min_score]

    print(f"All optimal paths with score {min_score}:")
    for path in best_paths:
        print(f"  {path}: {path_scores[path]}")

    return best_paths[0] + "A"


# print(len(get_most_optimal_path(goal="29")))
# exit()
# # 11
# p1 = ">^^"
# sp1 = get_shortest_paths_for_goal_remote(p1 + "A")
# sp1_next = []
# for p in sp1:
#     sp1_next += get_shortest_paths_for_goal_remote(p + "A")
# print(min([len(p) for p in sp1_next]))

# # 12
# p2 = "^^>"
# sp2 = get_shortest_paths_for_goal_remote(p2 + "A")
# sp2_next = []
# for p in sp2:
#     sp2_next += get_shortest_paths_for_goal_remote(p + "A")
# print(min([len(p) for p in sp2_next]))

# print(len(get_most_optimal_path(goal="A0")))
# print(len(get_most_optimal_path(goal="02")))
# print(len(get_most_optimal_path(goal="29")))
# print(len(get_most_optimal_path(goal="9A")))
# exit()
# keys = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A"]
# all_shortest_keypad_paths = {}
# for k1 in keys:
#     for k2 in keys:
#         print("Goal: ", k1 + k2)
#         goal = k1 + k2
#         all_shortest_keypad_paths[goal] = get_most_optimal_path(goal)
# print("*" * 60)
# print(all_shortest_keypad_paths)

# exit()
# Manually fixed one.
all_shortest_keypad_paths = {'00': 'A', '01': '^<A', '02': '^A', '03': '^>A', '04': '^<^A', '05': '^^A', '06': '>^^A', '07': '^<^^A', '08': '^^^A', '09': '>^^^A', '0A': '>A', '10': '>vA', '11': 'A', '12': '>A', '13': '>>A', '14': '^A', '15': '^>A', '16': '^>>A', '17': '^^A', '18': '>^^A', '19': '^^>>A', '1A': '>v>A', '20': 'vA', '21': '<A', '22': 'A', '23': '>A', '24': '<^A', '25': '^A', '26': '^>A', '27': '<^^A', '28': '^^A', '29': '>^^A', '2A': 'v>A', '30': '<vA', '31': '<<A', '32': '<A', '33': 'A', '34': '<<^A', '35': '<^A', '36': '^A', '37': '<<^^A', '38': '<^^A', '39': '^^A', '3A': 'vA', '40': '>vvA', '41': 'vA', '42': 'v>A', '43': 'v>>A', '44': 'A', '45': '>A', '46': '>>A', '47': '^A', '48': '^>A', '49': '^>>A', '4A': '>vv>A', '50': 'vvA', '51': '<vA', '52': 'vA', '53': 'v>A', '54': '<A', '55': 'A', '56': '>A', '57': '<^A', '58': '^A', '59': '^>A', '5A': 'vv>A', '60': '<vvA', '61': '<<vA', '62': '<vA', '63': 'vA', '64': '<<A', '65': '<A', '66': 'A', '67': '<<^A', '68': '<^A', '69': '^A', '6A': 'vvA', '70': '>vvvA', '71': 'vvA', '72': 'vv>A', '73': 'vv>>A', '74': 'vA', '75': 'v>A', '76': 'v>>A', '77': 'A', '78': '>A', '79': '>>A', '7A': '>vvv>A', '80': 'vvvA', '81': '<vvA', '82': 'vvA', '83': 'vv>A', '84': '<vA', '85': 'vA', '86': 'v>A', '87': '<A', '88': 'A', '89': '>A', '8A': 'vvv>A', '90': '<vvvA', '91': '<<vvA', '92': '<vvA', '93': 'vvA', '94': '<<vA', '95': '<vA', '96': 'vA', '97': '<<A', '98': '<A', '99': 'A', '9A': 'vvvA', 'A0': '<A', 'A1': '^<<A', 'A2': '<^A', 'A3': '^A', 'A4': '^^<<A', 'A5': '<^^A', 'A6': '^^A', 'A7': '^<<^^A', 'A8': '<^^^A', 'A9': '^^^A', 'AA': 'A'}

def get_most_optimal_path_remote(goal):
    assert len(goal) == 2
    pos0 = get_pos_remote(goal[0])
    pos1 = get_pos_remote(goal[1])
    if pos0 == pos1:
        return "A"
    paths = all_remote_paths[(pos0, pos1)]
    if len(paths) == 1:
        return paths[0] + "A"

    # Track scores for each original path
    path_scores = defaultdict(list)

    for original_path in paths:
        current_paths = [original_path]

        # Simulate n_remotes generations
        for gen in range(2):
            next_paths = []
            for p in current_paths:
                # Only add 'A' at the end
                remote_paths = get_shortest_paths_for_goal_remote(p + "A")
                next_paths.extend(remote_paths)

            # Track minimum length for this generation
            min_len = min(len(p) for p in next_paths) if next_paths else 0
            path_scores[original_path].append(min_len)
            current_paths = [p for p in next_paths if len(p) == min_len]

    # Choose the path that leads to shortest overall sequences
    best_path = min(path_scores.items(), key=lambda x: sum(x[1]))[0]
    return best_path + "A"

# keys = ["<", ">", "^", "v", "A"]
# all_shortest_remote_paths = {}
# for k1 in tqdm(keys):
#     for k2 in keys:
#         goal = k1 + k2
#         all_shortest_remote_paths[goal] = get_most_optimal_path_remote(goal)
# print("*" * 80)
# print(all_shortest_remote_paths)

all_shortest_remote_paths = {'<<': 'A', '<>': '>>A', '<^': '>^A', '<v': '>A', '<A': '>>^A', '><': '<<A', '>>': 'A', '>^': '<^A', '>v': '<A', '>A': '^A', '^<': 'v<A', '^>': 'v>A', '^^': 'A', '^v': 'vA', '^A': '>A', 'v<': '<A', 'v>': '>A', 'v^': '^A', 'vv': 'A', 'vA': '^>A', 'A<': 'v<<A', 'A>': 'vA', 'A^': '<A', 'Av': '<vA', 'AA': 'A'}
# exit()

@cache
def get_shortest_paths_for_goal_keypad_only_one(goal):
    result = ""
    for i in range(len(goal) - 1):
        start = goal[i]
        end = goal[i + 1]
        result += all_shortest_keypad_paths[start + end]

    return result

# print(all_shortest_keypad_paths)
# print(get_shortest_paths_for_goal_keypad_only_one("A029A"))

@cache
def get_shortest_paths_for_goal_remote_only_one(goal):
    result = ""
    for i in range(len(goal) - 1):
        start = goal[i]
        end = goal[i + 1]
        result += all_shortest_remote_paths[start + end]
    return result

# This is the method similar to before where we track the shortest path.
# p = get_shortest_paths_for_goal_keypad_only_one("A" + "379A")
# print('p1', p, len(p))
# p = get_shortest_paths_for_goal_remote_only_one("A" + p)
# print('p2', p, len(p))
# p = get_shortest_paths_for_goal_remote_only_one("A" + p)
# print('p3', p, len(p))


# print("*" * 60)
# print(all_shortest_remote_paths)

# These are not useful anymore since we moved to the same dictionary system as the
# usual utils, but I spent a lot of time on these and now emotionally attached.
"""
dict_remote = {
    "A": {
        "<": "^",
        "v": ">",
    },
    "^": {
        ">": "A",
        "v": "v",
    },
    "v": {
        "<": "<",
        ">": ">",
        "^": "^",
    },
    ">": {
        "^": "A",
        "<": "v"
    },
    "<": {
        ">": "v"
    }
}

dict_keypad = {
    "A": {
        "^": "3",
        "<": "0"
    },
    "0": {
        "^": "2",
        ">": "A"
    },
    "1": {
        "^": "4",
        ">": "2"
    },
    "2": {
        "^": "5",
        ">": "3",
        "<": "1",
        "v": "0"
    },
    "3": {
        "^": "6",
        "<": "2",
        "v": "A"
    },
    "4": {
        "^": "7",
        ">": "5",
        "v": "1"
    },
    "5": {
        "^": "8",
        ">": "6",
        "<": "4",
        "v": "2"
    },
    "6": {
        "^": "9",
        "<": "5",
        "v": "3",
    },
    "7": {
        ">": "8",
        "v": "4"
    },
    "8": {
        ">": "9",
        "<": "7",
        "v": "5"
    },
    "9": {
        "<": "8",
        "v": "6"
    },
}
"""

# Failled attempts to find most optimal, pair-wise paths.
# Is it feasible to test all combinations?
# 1795048117177052823552 -- no, not feasible.
# tot = 1
# for k, paths in all_keypad_paths.items():
#     min_path_dists = min([get_dist_path(path) for path in paths])
#     min_paths = [path for path in paths if get_dist_path(path) == min_path_dists]
#     tot *= len(min_paths)

# print(tot)

"""
# As long as we take the shortest one, I think we'd be okay. Nope.
all_shortest_keypad_paths = {}
for k, paths in all_keypad_paths.items():
    if len(paths) > 1:
        min_path_dists = min([get_dist_path(path) for path in paths])
        # all_shortest_keypad_paths[k] = [path for path in paths if get_dist_path(path) == min_path_dists][0]
        # Unfortunately this is not always the case so we will try to shuffle.
        # If we get the right answer we will lock the result.
        all_shortest_keypad_paths[k] = random.choice([path for path in paths if get_dist_path(path) == min_path_dists])
    else:
        all_shortest_keypad_paths[k] = paths[0]

# We can do the same for the remote paths.
all_shortest_remote_paths = {}
for k, paths in all_remote_paths.items():
    if len(paths) > 1:
        min_path_dists = min([get_dist_path(path) for path in paths])
        # all_shortest_remote_paths[k] = [path for path in paths if get_dist_path(path) == min_path_dists][0]
        all_shortest_remote_paths[k] = random.choice([path for path in paths if get_dist_path(path) == min_path_dists])
    else:
        all_shortest_remote_paths[k] = paths[0]


# print("*" * 40 + " KEYPAD " + "*" * 40)
# print(all_shortest_keypad_paths)
# print("*" * 40 + " REMOTE " + "*" * 40)
# print(all_shortest_remote_paths)
# print("." * 80)


# all_shortest_keypad_paths = {((0, 0), (0, 1)): '>', ((0, 0), (0, 2)): '>>', ((0, 0), (1, 0)): 'v', ((0, 0), (1, 1)): '>v', ((0, 0), (1, 2)): 'v>>', ((0, 0), (2, 0)): 'vv', ((0, 0), (2, 1)): '>vv', ((0, 0), (2, 2)): 'vv>>', ((0, 0), (3, 1)): '>vvv', ((0, 0), (3, 2)): '>>vvv', ((0, 1), (0, 0)): '<', ((0, 1), (0, 2)): '>', ((0, 1), (1, 0)): '<v', ((0, 1), (1, 1)): 'v', ((0, 1), (1, 2)): 'v>', ((0, 1), (2, 0)): 'vv<', ((0, 1), (2, 1)): 'vv', ((0, 1), (2, 2)): 'vv>', ((0, 1), (3, 1)): 'vvv', ((0, 1), (3, 2)): '>vvv', ((0, 2), (0, 0)): '<<', ((0, 2), (0, 1)): '<', ((0, 2), (1, 0)): 'v<<', ((0, 2), (1, 1)): '<v', ((0, 2), (1, 2)): 'v', ((0, 2), (2, 0)): 'vv<<', ((0, 2), (2, 1)): 'v<v', ((0, 2), (2, 2)): 'vv', ((0, 2), (3, 1)): '<vvv', ((0, 2), (3, 2)): 'vvv', ((1, 0), (0, 0)): '^', ((1, 0), (0, 1)): '^>', ((1, 0), (0, 2)): '^>>', ((1, 0), (1, 1)): '>', ((1, 0), (1, 2)): '>>', ((1, 0), (2, 0)): 'v', ((1, 0), (2, 1)): '>v', ((1, 0), (2, 2)): '>>v', ((1, 0), (3, 1)): '>vv', ((1, 0), (3, 2)): '>>vv', ((1, 1), (0, 0)): '^<', ((1, 1), (0, 1)): '^', ((1, 1), (0, 2)): '>^', ((1, 1), (1, 0)): '<', ((1, 1), (1, 2)): '>', ((1, 1), (2, 0)): '<v', ((1, 1), (2, 1)): 'v', ((1, 1), (2, 2)): '>v', ((1, 1), (3, 1)): 'vv', ((1, 1), (3, 2)): '>vv', ((1, 2), (0, 0)): '^<<', ((1, 2), (0, 1)): '<^', ((1, 2), (0, 2)): '^', ((1, 2), (1, 0)): '<<', ((1, 2), (1, 1)): '<', ((1, 2), (2, 0)): 'v<<', ((1, 2), (2, 1)): '<v', ((1, 2), (2, 2)): 'v', ((1, 2), (3, 1)): '<vv', ((1, 2), (3, 2)): 'vv', ((2, 0), (0, 0)): '^^', ((2, 0), (0, 1)): '^^>', ((2, 0), (0, 2)): '^^>>', ((2, 0), (1, 0)): '^', ((2, 0), (1, 1)): '^>', ((2, 0), (1, 2)): '>>^', ((2, 0), (2, 1)): '>', ((2, 0), (2, 2)): '>>', ((2, 0), (3, 1)): '>v', ((2, 0), (3, 2)): '>v>', ((2, 1), (0, 0)): '<^^', ((2, 1), (0, 1)): '^^', ((2, 1), (0, 2)): '>^^', ((2, 1), (1, 0)): '^<', ((2, 1), (1, 1)): '^', ((2, 1), (1, 2)): '^>', ((2, 1), (2, 0)): '<', ((2, 1), (2, 2)): '>', ((2, 1), (3, 1)): 'v', ((2, 1), (3, 2)): 'v>', ((2, 2), (0, 0)): '<<^^', ((2, 2), (0, 1)): '^^<', ((2, 2), (0, 2)): '^^', ((2, 2), (1, 0)): '<<^', ((2, 2), (1, 1)): '<^', ((2, 2), (1, 2)): '^', ((2, 2), (2, 0)): '<<', ((2, 2), (2, 1)): '<', ((2, 2), (3, 1)): '<v', ((2, 2), (3, 2)): 'v', ((3, 0), (0, 0)): '^^^', ((3, 0), (0, 1)): '>^^^', ((3, 0), (0, 2)): '>>^^^', ((3, 0), (1, 0)): '^^', ((3, 0), (1, 1)): '>^^', ((3, 0), (1, 2)): '^^>>', ((3, 0), (2, 0)): '^', ((3, 0), (2, 1)): '^>', ((3, 0), (2, 2)): '^>>', ((3, 0), (3, 1)): '>', ((3, 0), (3, 2)): '>>', ((3, 1), (0, 0)): '^<^^', ((3, 1), (0, 1)): '^^^', ((3, 1), (0, 2)): '^^^>', ((3, 1), (1, 0)): '^^<', ((3, 1), (1, 1)): '^^', ((3, 1), (1, 2)): '^^>', ((3, 1), (2, 0)): '^<', ((3, 1), (2, 1)): '^', ((3, 1), (2, 2)): '^>', ((3, 1), (3, 2)): '>', ((3, 2), (0, 0)): '^^<<^', ((3, 2), (0, 1)): '<^^^', ((3, 2), (0, 2)): '^^^', ((3, 2), (1, 0)): '^^<<', ((3, 2), (1, 1)): '^<^', ((3, 2), (1, 2)): '^^', ((3, 2), (2, 0)): '^<<', ((3, 2), (2, 1)): '<^', ((3, 2), (2, 2)): '^', ((3, 2), (3, 1)): '<'}
# all_shortest_remote_paths = {((0, 0), (0, 1)): '>', ((0, 0), (0, 2)): '>>', ((0, 0), (1, 0)): 'v', ((0, 0), (1, 1)): '>v', ((0, 0), (1, 2)): '>>v', ((0, 1), (0, 2)): '>', ((0, 1), (1, 0)): 'v<', ((0, 1), (1, 1)): 'v', ((0, 1), (1, 2)): '>v', ((0, 2), (0, 1)): '<', ((0, 2), (1, 0)): 'v<<', ((0, 2), (1, 1)): 'v<', ((0, 2), (1, 2)): 'v', ((1, 0), (0, 1)): '>^', ((1, 0), (0, 2)): '>>^', ((1, 0), (1, 1)): '>', ((1, 0), (1, 2)): '>>', ((1, 1), (0, 1)): '^', ((1, 1), (0, 2)): '^>', ((1, 1), (1, 0)): '<', ((1, 1), (1, 2)): '>', ((1, 2), (0, 1)): '^<', ((1, 2), (0, 2)): '^', ((1, 2), (1, 0)): '<<', ((1, 2), (1, 1)): '<'}
"""
