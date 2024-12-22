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
from collections import defaultdict
import heapq
import utils

dirs = [">", "<", "^", "v"]

def get_pos(dict_board, value):
    """Quick conversion to go from, e.g., A to (i, j)."""
    return next((pos for pos, val in dict_board.items() if val == value), None)


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



def get_shortest_paths_for_goal(goal, dict_board, all_paths):
    """Get all shortest paths for reaching a goal (str)."""
    result = [""]
    for i in range(len(goal) - 1):
        start = goal[i]
        end = goal[i + 1]
        start_pos = get_pos(dict_board, start)
        end_pos = get_pos(dict_board, end)
        if start_pos == end_pos:
            # Already there, then just press the button.
            result = [r + "A" for r in result]
        else:
            paths = all_paths[(start_pos, end_pos)]
            # Add the path to every path in result.
            new_result = []
            for r in result:
                for p in paths:
                    # Add the "A" for button press.
                    new_result.append(r + p + "A")
            result = new_result

    return [r for r in result if r]



# These are not useful anymore since we moved to the same dictionary system as the
# usual utils, but I spent a lot of time on these and now emotionally attached.
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

