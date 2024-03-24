# Problem type:
# ~~~~~~~~~~~~ LONG PROBLEM IS LONG ~~~~~~~~~~~~
# This one took the longest out of all 2017 problems (although I'd say day 23
# part 2 is the hardest). Just a lot of matrix utility functions to set up, even
# with the help of numpy.
from mat_utils import *

dict_rules = get_rules()

pattern = """\
.#.
..#
###
""".splitlines()

list_rows = get_list_rows(pattern)

for _ in range(5):
    list_rows = enhance(list_rows, dict_rules)

# Count num on.
cnt = 0
for row in list_rows:
    for r in row:
        if r == "#":
            cnt += 1

print("Part 1:", cnt)


# Part 2, reset.
from tqdm import tqdm
list_rows = get_list_rows(pattern)

for _ in tqdm(range(18)):
    list_rows = enhance(list_rows, dict_rules)

# Count num on.
cnt = 0
for row in list_rows:
    for r in row:
        if r == "#":
            cnt += 1

print("Part 2:", cnt)
