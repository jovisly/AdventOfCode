# Problem type:
# ~~~~~~~~~~~~ bug fest ~~~~~~~~~~~~
# Related to Day 10. But turns out I had a bug back in Day 10 that was not caught.
# This bug was not padding hex value with 0. Which did not impact part 1, but for
# part 2, the bug manifested.


import utils
from day_10 import get_full_seq

# For testing
key_str = "flqrgnkx"
key_str = "ffayrhll"

dim = 128
tot = 0
dict_board = {}
for i in range(dim):
    full_key_str = key_str + "-" + str(i)
    fs = get_full_seq(full_key_str)
    tot += fs.count("1")
    for j, v in enumerate(list(fs)):
        dict_board[(i, j)] = v


# print("dict board looks fishy")
# print("dict_board[(0, 0)]", dict_board[(0, 0)])
# print("dict_board[(0, 1)]", dict_board[(0, 1)])
# print("dict_board[(0, 2)]", dict_board[(0, 2)])
# print("")
# print("dict_board[(1, 0)]", dict_board[(1, 0)])
# print("dict_board[(1, 1)]", dict_board[(1, 1)])
# print("dict_board[(1, 2)]", dict_board[(1, 2)])
# print("")
# print("dict_board[(2, 0)]", dict_board[(2, 0)])
# print("dict_board[(2, 1)]", dict_board[(2, 1)])
# print("dict_board[(2, 2)]", dict_board[(2, 2)])


print("Part 1:", tot)

num_on = len([v for v in dict_board.values() if v == "1"])

# Start with something that's on.
curr_pos = [k for k, v in dict_board.items() if v == "1"][0]
curr_pos = (0, 0)
visited = set(curr_pos)
list_group = [curr_pos]
num_groups = 1


while len(visited) != num_on:
    # Spread.
    neighbors = []
    for p in list_group:
        ns = utils.get_neighbors(p)
        ns = [
            n for n in ns
            if n not in list_group
            and n not in visited
            and n in dict_board
            and dict_board[n] == "1"
            and n not in neighbors
        ]
        neighbors += ns

    # Are there any new neighbors?
    if len(neighbors) == 0:
        # No new neighbor. Pick a new pos and increment num groups.
        # print("list group:", list_group)

        curr_pos = [
            k for k, v in dict_board.items()
            if v == "1" and k not in visited
        ][0]
        list_group = [curr_pos]
        visited.add(curr_pos)
        num_groups += 1
        if num_groups % 100 == 0:
            print(" ... num groups:", num_groups)
    else:
        # Continue spreading this group.
        for n in neighbors:
            visited.add(n)

        list_group += list(set(neighbors))


print("Part 2:", num_groups)
# 1133 is too low. because we need to add 1. When do we add 1 depends on situation.
