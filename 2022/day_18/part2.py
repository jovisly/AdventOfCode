"""
Time: 45m (with a pretty big hint)

Bug report:

I kept trying to figure out a way to identify "inside" the cubes, but got
nowhere. I was also very worried about complex cubes topology like winding
tunnels inside the cubes. Finally I got a hint to "think outside the box", which
helpfully took my attention to the outside, instead of inside.

After getting the list of "outside" positions, I got the wrong answer. This was
caused by not having a buffer around the min and max positions, meaning there're
some valid outside positions being missed. After adding buffer, it worked just
fine.

My implementation is very straightforward and not optimized. For the actual
dataset it ran in about 20 seconds.
"""
from tqdm import tqdm
from part1 import get_cubes


def get_min_max(cubes):
    min_x = min(cubes, key=lambda x: x[0])[0]
    max_x = max(cubes, key=lambda x: x[0])[0]
    min_y = min(cubes, key=lambda x: x[1])[1]
    max_y = max(cubes, key=lambda x: x[1])[1]
    min_z = min(cubes, key=lambda x: x[2])[2]
    max_z = max(cubes, key=lambda x: x[2])[2]

    return min_x, max_x, min_y, max_y, min_z, max_z


def get_outside(cubes):
    min_x, max_x, min_y, max_y, min_z, max_z = get_min_max(cubes)
    # Give it a little bit of buffer.
    buffer = 2
    min_x -= buffer
    max_x += buffer
    min_y -= buffer
    max_y += buffer
    min_z -= buffer
    max_z += buffer

    outside = set()
    queue = [(min_x, min_y, min_z)]
    while len(queue) > 0:
        x, y, z = queue.pop()

        if x < min_x or x > max_x or y < min_y or y > max_y or z < min_z or z > max_z:
            continue

        if (x, y, z) in cubes:
            continue

        if (x, y, z) in outside:
            continue

        outside.add((x, y, z))

        queue.append((x + 1, y, z))
        queue.append((x - 1, y, z))
        queue.append((x, y + 1, z))
        queue.append((x, y - 1, z))
        queue.append((x, y, z + 1))
        queue.append((x, y, z - 1))

    return list(outside)



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    cubes = get_cubes(lines)

    # Plan: start with a position that is "outside", and within the boundary of
    # min and max, visit all its neighbors. What this will give us is a set of
    # positions that are "outside" the cubes. Then we can count the cubes
    # surfaces like before, but only if they are in touch with the "outside"
    # positions.
    outside = get_outside(cubes)


    # Now we do similar inefficient n x m check, but this time we count only
    # faces that are "touching" an outside position.
    grand_total = 0
    for i in tqdm(range(len(cubes))):
        faces = {
            "xp": 0,
            "xm": 0,
            "yp": 0,
            "ym": 0,
            "zp": 0,
            "zm": 0,
        }
        ci = cubes[i]

        for j in range(len(outside)):
            cj = outside[j]

            if cj[0] == ci[0] + 1 and cj[1] == ci[1] and cj[2] == ci[2]:
                faces["xp"] = 1

            if cj[0] == ci[0] - 1 and cj[1] == ci[1] and cj[2] == ci[2]:
                faces["xm"] = 1

            if cj[1] == ci[1] + 1 and cj[0] == ci[0] and cj[2] == ci[2]:
                faces["yp"] = 1

            if cj[1] == ci[1] - 1 and cj[0] == ci[0] and cj[2] == ci[2]:
                faces["ym"] = 1

            if cj[2] == ci[2] + 1 and cj[0] == ci[0] and cj[1] == ci[1]:
                faces["zp"] = 1

            if cj[2] == ci[2] - 1 and cj[0] == ci[0] and cj[1] == ci[1]:
                faces["zm"] = 1

        # Add up remaining faces.
        total = sum(faces.values())
        grand_total += total

    print("grand_total", grand_total)
    return grand_total


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 58


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
