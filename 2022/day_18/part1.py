"""
Time: 15m

Bug report:

Originally I was only checking cj[0] == ci[0] + 1 without imposing that the
other two coordinates were the same, which lead to the wrong answer.
"""
from tqdm import tqdm

def get_cubes(lines):
    cubes = []
    for item in lines:
        cube = item.split(",")
        cube = [int(x) for x in cube]
        cubes.append(tuple(cube))
    return cubes


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    cubes = get_cubes(lines)
    grand_total = 0

    # We will do a very inefficient n x n lookup.
    for i in tqdm(range(len(cubes))):
        faces = {
            "xp": 1,
            "xm": 1,
            "yp": 1,
            "ym": 1,
            "zp": 1,
            "zm": 1,
        }
        ci = cubes[i]

        for j in range(len(cubes)):
            if i == j:
                continue

            cj = cubes[j]

            if cj[0] == ci[0] + 1 and cj[1] == ci[1] and cj[2] == ci[2]:
                faces["xp"] = 0

            if cj[0] == ci[0] - 1 and cj[1] == ci[1] and cj[2] == ci[2]:
                faces["xm"] = 0

            if cj[1] == ci[1] + 1 and cj[0] == ci[0] and cj[2] == ci[2]:
                faces["yp"] = 0

            if cj[1] == ci[1] - 1 and cj[0] == ci[0] and cj[2] == ci[2]:
                faces["ym"] = 0

            if cj[2] == ci[2] + 1 and cj[0] == ci[0] and cj[1] == ci[1]:
                faces["zp"] = 0

            if cj[2] == ci[2] - 1 and cj[0] == ci[0] and cj[1] == ci[1]:
                faces["zm"] = 0

        # Add up remaining faces.
        total = sum(faces.values())
        grand_total += total

    print("grand_total", grand_total)
    return grand_total


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 64

    filename = "input-test2.txt"
    assert solve(filename) == 10


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
