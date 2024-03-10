# Problem type:
# ~~~~~~~~~~~~ mild physics ~~~~~~~~~~~~
# Reminds me of https://adventofcode.com/2023/day/24, but this one is much nicer
# and doesn't require solving for intersections since we can treat time as
# discrete.
filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

def get_vec(line, i):
    vec = line.split(", ")[i].split("=")[-1][1:-1].split(",")
    vec = [int(v) for v in vec]
    assert len(vec) == 3
    return vec[0], vec[1], vec[2]


# x(t) = x0 + v0*t + 0.5*a*t^2
# manhattan dist: abs(x(t)) + abs(y(t)) + abs(z(t))
# and we can choose a big t.
# This doesn't work. Seems like the numerical approximation aspect is making it
# slightly off. In that case we might just have to propagate. Nope, it doesn't
# work simply because i had a bug in get_vec() where i wasn't passing in the i.
T = 10**4
def pos_at_t(x0, v0, a, t=T):
    return x0 + v0 * t + 0.5 * a * (t**2)

min_dist = None
min_dist_ind = None
for ind, line in enumerate(lines):
    px, py, pz = get_vec(line, 0)
    vx, vy, vz = get_vec(line, 1)
    ax, ay, az = get_vec(line, 2)
    dist = (
        abs(pos_at_t(px, vx, ax)) +
        abs(pos_at_t(py, vy, ay)) +
        abs(pos_at_t(pz, vz, az))
    )
    # print(f"ind: {ind}, dist: {dist}")

    if min_dist is None or dist < min_dist:
        min_dist = dist
        min_dist_ind = ind
        # print(f"ind {ind}:", dist, line)

print("Part 1:", min_dist_ind)

# Part 2:
# I suppose we should use the propagated version instead of numerical. We also
# don't need to track id anymore.
from collections import Counter
import copy
from tqdm import tqdm

def get_next_pos(p, v, a):
    v += a
    p += v
    return p, v, a


def get_next_pos_full(pos, vel, acc):
    px, py, pz = pos
    vx, vy, vz = vel
    ax, ay, az = acc

    px2, vx2, ax2 = get_next_pos(px, vx, ax)
    py2, vy2, ay2 = get_next_pos(py, vy, ay)
    pz2, vz2, az2 = get_next_pos(pz, vz, az)
    return (px2, py2, pz2), (vx2, vy2, vz2), (ax2, ay2, az2)

# We prob don't need this.
def pos_at_t(x0, v0, a, t=T):
    p, v, a = x0, v0, a
    for _ in range(t):
        p, v, a = get_next_pos(p, v, a)
    return p

# Set up dictionaries to track positions.
dict_pos = {}
for i, line in enumerate(lines):
    px, py, pz = get_vec(line, 0)
    vx, vy, vz = get_vec(line, 1)
    ax, ay, az = get_vec(line, 2)
    dict_pos[i] = ((px, py, pz), (vx, vy, vz), (ax, ay, az))

# Are any of them at same position? Ok initial positions are all unique.
cnts = Counter([v[0] for v in dict_pos.values()])
assert max(cnts.values()) == 1

for _ in tqdm(range(10**2)):
    dict_prev = copy.deepcopy(dict_pos)
    dict_pos = {}
    for k, v in dict_prev.items():
        pos, vel, acc = v
        pos, vel, acc = get_next_pos_full(pos, vel, acc)
        dict_pos[k] = (pos, vel, acc)
    # Check collision.
    cnts = Counter([v[0] for v in dict_pos.values()])
    bad_pos = []
    for pos, c in cnts.items():
        if c > 1:
            bad_pos.append(pos)
    bad_k = []
    for pos in bad_pos:
        for k, v in dict_pos.items():
            if v[0] == pos:
                bad_k.append(k)
    for k in bad_k:
        del dict_pos[k]

# Takes 1.5 min for 10**4 but actually 10**2 is enough.
print("Part 2:", len(dict_pos))
