import hashlib
import heapq
import utils

PASSCODE = "hijkl"  # does not have a path.
PASSCODE = "ihgpwlah"
PASSCODE = "kglvqrro"
PASSCODE = "ulqzkmiv"
PASSCODE = "gdjjyniy"
START = (0, 0)
END = (3, 3)

POSITIONS = []
for i in range(4):
    for j in range(4):
        POSITIONS.append((i, j))


def get_pos(path, start=START):
    steps = list(path)
    pos = start
    for step in steps:
        pos = utils.move_to_dir(pos, step)
    return pos


def get_md5(passcode):
    hashed = hashlib.md5(passcode.encode("utf-8"))
    return hashed.hexdigest()


def get_dirs(steps="", passcode=PASSCODE):
    fullpass = passcode + steps
    md5 = get_md5(fullpass)[:4]
    status = [m in ["b", "c", "d", "e", "f"] for m in list(md5)]
    dirs = ["U", "D", "L", "R"]
    return [d for i, d in enumerate(dirs) if status[i] == True]


if __name__ == "__main__":
    queue = [(0, "")]
    visited = {""}

    while len(queue) > 0:
        curr_cost, curr_path = heapq.heappop(queue)
        curr_pos = get_pos(curr_path)

        if curr_pos == END:
            print("FOUND!", curr_path)
            exit()

        dirs = get_dirs(steps=curr_path)
        for dir in dirs:
            new_path = curr_path + dir
            new_pos = get_pos(new_path)
            if new_path not in visited and new_pos in POSITIONS:
                heapq.heappush(queue, (curr_cost + 1, new_path))
                visited.add(new_path)

    print("No path found.")
