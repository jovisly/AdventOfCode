import re
from tqdm import tqdm

def get_sb(line):
    return [tuple(map(int, pair)) for pair in re.findall(r'x=(-?\d+), y=(-?\d+)', line)]


def get_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def is_bad_pos(pos, list_bs_dist, list_sb, list_b):
    if pos in list_b:
        return 0
    list_dist = [get_dist(s, pos) for s, b in list_sb]
    for a, b in zip(list_bs_dist, list_dist):
        if b <= a:
            return 1

    return 0



def solve(filename, y):
    lines = open(filename, encoding="utf-8").read().splitlines()
    list_sb = [get_sb(line) for line in lines]
    list_b = [b for s, b in list_sb]

    list_bs_dist = [get_dist(b, s) for b, s in list_sb]
    min_x = min(
        [b[0] for s, b in list_sb] +
        [s[0] for s, b in list_sb]
    )
    max_x = max(
        [b[0] for s, b in list_sb] +
        [s[0] for s, b in list_sb]
    )

    # Let's be generous. This is because we're not sure if the beacon is in the
    # range. It depends on what other further beacons are there. But +/- 50%
    # should be enough.
    min_x = min_x - (max_x - min_x) // 2
    max_x = max_x + (max_x - min_x) // 2

    num_cannot_be = 0
    for x in tqdm(range(min_x, max_x + 1)):
        pos = (x, y)
        num_cannot_be += is_bad_pos(pos, list_bs_dist, list_sb, list_b)

    print("num_cannot_be:", num_cannot_be)
    return num_cannot_be


def mini_test():
    filename = "input-test.txt"
    assert solve(filename, y=10) == 26


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename, y=2000000)

    print(total)
