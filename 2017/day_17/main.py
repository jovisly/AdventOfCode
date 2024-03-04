# Problem type:
# ~~~~~~~~~~~~ english comprehension (part 1) ~~~~~~~~~~~~
# the sentence "inserts **after** it" is extremely confusing. you step "forward",
# yet the "insert *after*" is also forward...
# ~~~~~~~~~~~~ thinker + optimizer (part 2) ~~~~~~~~~~~~
# at first i thought part 2 is "find the pattern" again but i couldn't find one.
# then realized we don't actually have to do array updates so going through 50M
# can be done much faster.

# For testing.
puzzle_input = 3
puzzle_input = 337
num = 2017

curr_pos = 0
curr_arr = [0]

for i in range(num):
    # Step forward.
    # for _ in range(puzzle_input):
    #     curr_pos = (curr_pos + 1) % len(curr_arr)
    curr_pos = (curr_pos + puzzle_input) % len(curr_arr)
    # Add the value.
    v = i + 1
    if curr_pos == len(curr_arr) - 1:
        curr_arr += [v]
        curr_pos = len(curr_arr) - 1
    else:
        curr_arr = curr_arr[:curr_pos + 1] + [v] + curr_arr[curr_pos + 1:]
        curr_pos = curr_pos + 1


print("Part 1:", curr_arr[curr_pos + 1])

# Reset for part 2. I guess 5M is still waitable... NOPE! The issue is that arr
# operation is very slow especially we keep reconstructing it. Maybe all we do
# is track position and arr length. It's actually the same as before except we
# don't do any array update.
from tqdm import tqdm
curr_pos = 0
curr_arr_length = 1

for i in tqdm(range(50 * 10**6)):
# for i in range(5 * 10**4):
    # Step forward.
    curr_pos = (curr_pos + puzzle_input) % curr_arr_length

    # Add the value.
    if curr_pos == curr_arr_length - 1:
        curr_arr_length += 1
        curr_pos = curr_arr_length - 1
    else:
        curr_arr_length += 1
        curr_pos = curr_pos + 1

    if curr_pos == 1:
        last_v = i + 1
        # print(last_v)

print("Part 2:", last_v)
exit()
# 4771057 is too low; 4771058 also too low. Oh because we want 50M not 5M.
# for i in tqdm(range(50000000)):
ns = set()
for i in range(100000):
    # Step forward.
    for _ in range(puzzle_input):
        curr_pos = (curr_pos + 1) % len(curr_arr)
    # Add the value.
    v = i + 1
    if curr_pos == len(curr_arr) - 1:
        curr_arr += [v]
        curr_pos = len(curr_arr) - 1
    else:
        curr_arr = curr_arr[:curr_pos + 1] + [v] + curr_arr[curr_pos + 1:]
        curr_pos = curr_pos + 1

    ind = curr_arr.index(0)
    n = curr_arr[1]
    if n not in ns:
        ns.add(n)
        print(i + 1, curr_arr[:2])
    assert curr_arr[0] == 0


"""
# Any pattern? Not seeing anything. Maybe let's think about when do we end up at
# the 0-th position? because that's when we'd get to add a new item after.
1 [0, 1]
2 [0, 2]
4 [0, 4]
7 [0, 7]
16 [0, 16]
33 [0, 33]
146 [0, 146]
483 [0, 483]
9754 [0, 9754]
17280 [0, 17280]
27434 [0, 27434]
28427 [0, 28427]
"""
