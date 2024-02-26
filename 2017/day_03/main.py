import utils

# There's a pattern of:
# 1
# 2 R 1
# 3 U 1
#   L 2
#   D 2
#   R 3
#   U 3
#   L 4
#   D 4

# So let's see if we can generate a sequence of steps like:
# R U LL DD RRRR UUUU LLLL DDDD RRRRR UUUUU...

num = 277678

steps = ""
rep = 1
dirs = "RU"
while len(steps) < num:
    for dir in list(dirs):
        steps += rep * dir

    rep += 1
    if dirs == "RU":
        dirs = "LD"
    else:
        dirs = "RU"

# To get to num, we need num - 1 steps.
steps = steps[:num - 1]
pos = (0, 0)

for s in list(steps):
    pos = utils.move_to_dir(pos, s)

print("Part 1:", abs(pos[0]) + abs(pos[1]))


# For Part 2, don't know how long the steps need to be but I don't think it'd be
# longer than num (since we are adding up all previous numbers that are neighbors).
# So get the steps again; same thing as above.
num = 277678

steps = ""
rep = 1
dirs = "RU"
while len(steps) < num:
    for dir in list(dirs):
        steps += rep * dir

    rep += 1
    if dirs == "RU":
        dirs = "LD"
    else:
        dirs = "RU"

pos = (0, 0)
n = 1
dict_nums = {pos: 1}
for s in list(steps):
    pos = utils.move_to_dir(pos, s)
    neighbors = utils.get_neighbors(pos, num_dirs=8)
    neighbors = [n for n in neighbors if n in dict_nums]
    tot = sum([dict_nums[n] for n in neighbors])
    # print(tot)
    # input()
    if tot > num:
        print("Part 2:", tot)
        exit()
    dict_nums[pos] = tot


