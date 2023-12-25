import z3
from tqdm import tqdm

from part1 import get_sb, get_dist, is_bad_pos


def is_good_pos(pos, list_bs_dist, list_sb, list_b):
    if pos in list_b:
        return False
    list_dist = [get_dist(s, pos) for s, b in list_sb]
    for a, b in zip(list_bs_dist, list_dist):
        if b <= a:
            return False

    return True


def get_dist_z3(val):
    return z3.If(val >= 0, val, -1 * val)


def solve(filename, min_coord, max_coord):
    lines = open(filename, encoding="utf-8").read().splitlines()
    lines = open(filename, encoding="utf-8").read().splitlines()
    list_sb = [get_sb(line) for line in lines]
    list_b = [b for s, b in list_sb]
    list_bs_dist = [get_dist(b, s) for b, s in list_sb]

    # Brute force will be too slow.
    # for x in tqdm(range(min_coord, max_coord + 1)):
    #     for y in range(min_coord, max_coord + 1):
    #         pos = (x, y)
    #         result = is_good_pos(pos, list_bs_dist, list_sb, list_b)
    #         if result == True:
    #             return 4000000 * x + y
    z3_solver = z3.Solver()
    x, y = z3.Int("x"), z3.Int("y")
    z3_solver.add(x >= min_coord)
    z3_solver.add(x <= max_coord)
    z3_solver.add(y >= min_coord)
    z3_solver.add(y <= max_coord)

    for s, b in list_sb:
        dist = get_dist(s, b)
        z3_solver.add(get_dist_z3(s[0] - x) + get_dist_z3(s[1] - y) > dist)

    print("Model check:")
    print(z3_solver.check())
    print("Model:")
    print(z3_solver.model())
    return 0


def mini_test():
    filename = "input-test.txt"
    assert solve(filename, min_coord=0, max_coord=20) == 56000011


if __name__ == "__main__":
    # mini_test()

    filename = "input.txt"
    total = solve(filename, min_coord=0, max_coord=4000000)

    print(total)
