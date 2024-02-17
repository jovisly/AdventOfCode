import heapq

from part1 import get_pos, get_dirs, POSITIONS

PASSCODE = "ihgpwlah"
PASSCODE = "kglvqrro"
PASSCODE = "ulqzkmiv"
PASSCODE = "gdjjyniy"
START = (0, 0)
END = (3, 3)

queue = [""]
visited = {""}
max_path = 0

while len(queue) > 0:
    curr_path = heapq.heappop(queue)
    curr_pos = get_pos(curr_path)

    if curr_pos == END:
        # Keep track of the longest path but do exhaustive search.
        path_length = len(curr_path)
        if path_length > max_path:
            max_path = path_length
    else:
        dirs = get_dirs(steps=curr_path, passcode=PASSCODE)
        for dir in dirs:
            new_path = curr_path + dir
            new_pos = get_pos(new_path)
            if new_path not in visited and new_pos in POSITIONS:
                heapq.heappush(queue, new_path)
                visited.add(new_path)

print("Max:", max_path)
