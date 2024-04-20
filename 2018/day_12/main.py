# Problem type:
# ~~~~~~~ PATTERN MATCHING ~~~~~~~

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

PADDING = 80


def get_initial_state(lines):
    line = lines[0]
    segs = line.split("initial state: ")
    return segs[1]


def get_dict_mapping(lines):
    m_lines = lines[2:]
    dict_mapping = {}
    for line in m_lines:
        segs = line.split(" => ")
        dict_mapping[segs[0]] = segs[1]
    return dict_mapping


def get_next_gen(this_state, dict_mapping):
    pos = list(this_state)
    new_state = ""
    for i in range(len(pos)):
        s = i - 2
        e = i + 2
        if s >= 0 and e < len(pos):
            seg = pos[s:e + 1]
            if "".join(seg) in dict_mapping:
                new_state += dict_mapping["".join(seg)]
            else:
                new_state += "."
        else:
            new_state += "."
    return new_state


this_state = get_initial_state(lines)
this_state = "." * PADDING + this_state + "." * PADDING

dict_mapping = get_dict_mapping(lines)

for _ in range(20):
    this_state = get_next_gen(this_state, dict_mapping)
    # print(this_state)


# print(this_state)
s = 0
for i, c in enumerate(list(this_state)):
    if c == "#":
        # print("i - PADDING:", i - PADDING, i)
        s += i - PADDING


print("Part 1:", s)

# Part 2: 50000000000 generations. Clearly we won't run this many iterations. So
# let's try to find some pattern. We are also going to use a much bigger padding.
PADDING2 = 10000

def get_s(this_state):
    s = 0
    for i, c in enumerate(list(this_state)):
        if c == "#":
            s += i - PADDING2
    return s



this_state = get_initial_state(lines)
this_state = "." * PADDING2 + this_state + "." * PADDING2

# Looks like it becomes linear. So grateful!
# for i in range(5000):
#     this_state = get_next_gen(this_state, dict_mapping)
#     s = get_s(this_state)
#     if i % 100 == 0:
#         print(i, s)

"""
4800 38365
4900 39165
"""
n = 39165 - 38365
goal = 50000000000

print("Part 2:", int(39165 + n * ((goal - 4900) / 100 - 1)))
# 399500000014 is too low.
# 399999960800 is too low.
# 399999999165 is still not right.
# 399999999957
# 399999999965 is too high lol we are close.
# maybe we are not suppose to count the last generation (off by 1).

# ok let's just do an honest linear fit.
"""
import numpy as np

x = x[10:]
y = y[10:]

m, b = np.polyfit(x, y, 1)

x_predict = 50000000000 - 1
y_predict = m * x_predict + b
print(y_predict)
"""

