# Problem type:
# ~~~~~~~~~~~~ TIL ~~~~~~~~~~~~
# Hexagons are everywhere. From takenoko to x-ray crystallography. But I haven't
# had to code about it (i think?) until now. Moments like this make me feel very
# grateful to AoC. Like many before me, i ended up on redblobgames (again!) to
# shop for a coordinate system. I tried out a few before settling on the double
# height system. Then by pattern recognition i added the distance function,
# which is just a manhattan, but unfortunately that worked for all test cases
# yet is actually wrong because i didn't read far enough on the page.

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()
line = lines[0]

# For testing...
# line = "ne,ne,ne"
# line = "ne,ne,sw,sw"
# line = "ne,ne,s,s"
# line = "se,sw,se,sw,sw"

def move_to_dir(pos, dir):
    # Using the "double-height" horizontal layout from
    # https://www.redblobgames.com/grids/hexagons/
    if dir == "n":
        return (pos[0], pos[1] - 2)
    elif dir == "ne":
        return (pos[0] + 1, pos[1] - 1)
    elif dir == "se":
        return (pos[0] + 1, pos[1] + 1)
    elif dir == "s":
        return (pos[0], pos[1] + 2)
    elif dir == "sw":
        return (pos[0] - 1, pos[1] + 1)
    elif dir == "nw":
        return (pos[0] - 1, pos[1] - 1)
    else:
        raise ValueError(f"Unknown directions: {dir}")



def get_dist_wrong(pos):
    return (abs(pos[0]) + abs(pos[1])) / 2


def get_dist(pos):
    # https://www.redblobgames.com/grids/hexagons/#distances-doubled
    # Specifically, the doubleheight_distance
    dcol = abs(pos[0])
    drow = abs(pos[1])
    return dcol + max(0, (drow - dcol)/2)

steps = line.split(",")
pos = (0, 0)
for step in steps:
    pos = move_to_dir(pos, step)

print("Part 1:", get_dist(pos))


max_dist = 0
pos = (0, 0)
for step in steps:
    pos = move_to_dir(pos, step)
    dist = get_dist(pos)
    if dist > max_dist:
        max_dist = dist

print("Part 2:", max_dist)
