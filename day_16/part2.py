from tqdm import tqdm
from part1 import go_to_next, is_valid_pos


def get_num_energized(layout, initial_pos, initial_dir, max_step=100):
    rays = [(initial_pos, initial_dir)]
    energized = set()
    num_energized = len(energized)
    num_since_last_update = 0

    while len(rays) != 0 and num_since_last_update < max_step:
        new_rays = []
        for r in rays:
            energized.add(r[0])
            new_rays += go_to_next(layout, r)

        new_rays = {r for r in new_rays if is_valid_pos(layout, r[0])}
        rays = new_rays

        if len(energized) > num_energized:
            num_since_last_update = 0
            num_energized = len(energized)
        else:
            num_since_last_update += 1

    return len(energized)



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    layout = [list(l) for l in lines]

    max_num_energized = 0
    # From top row going down.
    for i in tqdm(range(len(layout[0]))):
        out = get_num_energized(layout=layout, initial_pos=(0, i), initial_dir="d")
        if out > max_num_energized:
            max_num_energized = out

    # From bottom row going up.
    for i in tqdm(range(len(layout[0]))):
        out = get_num_energized(layout=layout, initial_pos=(len(layout) - 1, i), initial_dir="u")
        if out > max_num_energized:
            max_num_energized = out

    # From left column going right.
    for i in tqdm(range(len(layout))):
        out = get_num_energized(layout=layout, initial_pos=(i, 0), initial_dir="r")
        if out > max_num_energized:
            max_num_energized = out

    # From right column going left.
    for i in tqdm(range(len(layout))):
        out = get_num_energized(layout=layout, initial_pos=(i, len(layout[0]) - 1), initial_dir="l")
        if out > max_num_energized:
            max_num_energized = out

    return max_num_energized


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 51


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
