import utils

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

l1 = lines[0]
l2 = lines[1]

# For testing.
# l1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
# l2 = "U62,R66,U55,R34,D71,R55,D58,R83"
# l1 = "R8,U5,L5,D3"
# l2 = "U7,R6,D4,L4"

l1 = l1.split(",")
l2 = l2.split(",")

# print(l1)

def get_locs(steps):
    pos = (0,0)
    # Originally had a list for this but wow speed of list membership check vs
    # set is so crazy different.
    locs = set()
    for s in steps:
        dir = s[0]
        num = int(s[1:])
        for _ in range(num):
            pos = utils.move_to_dir(pos, dir)
            locs.add(pos)
    return locs

locs1 = get_locs(l1)
locs2 = get_locs(l2)
overlaps = [l for l in locs1 if l in locs2]

dist = [abs(o[0]) + abs(o[1]) for o in overlaps]
print("Part 1:", min(dist))


# Part 2 -- need to know step num.
def get_dict_locs(steps):
    pos = (0, 0)
    dict_locs = {}
    n = 0
    for s in steps:
        dir = s[0]
        num = int(s[1:])
        for _ in range(num):
            n += 1
            pos = utils.move_to_dir(pos, dir)
            if pos not in dict_locs:
                dict_locs[pos] = n
    return dict_locs


dict_locs1 = get_dict_locs(l1)
dict_locs2 = get_dict_locs(l2)
overlaps = [k for k in dict_locs1.keys() if k in dict_locs2.keys()]
vals = [dict_locs1[k] + dict_locs2[k] for k in overlaps]
print("Part 2:", min(vals))
