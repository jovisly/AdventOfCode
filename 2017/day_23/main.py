# Problem type:
# ~~~~~~~~~~~~ follow instruction (part 1) ~~~~~~~~~~~~
# ~~~~~~~~~~~~ wow really need to think!!! (part 2) ~~~~~~~~~~~~
from collections import defaultdict

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

dict_reg = defaultdict(int)


def get_val(orig, dict_reg):
    if orig.replace("-", "").isdigit():
        return int(orig)
    else:
        return dict_reg[orig]


i = 0
cnt = 0
while i < len(lines) and i >= 0:
    inst = lines[i]
    segs = inst.split(" ")
    op = segs[0]
    v1 = get_val(segs[1], dict_reg)
    v2 = get_val(segs[2], dict_reg)

    if op == "set":
        dict_reg[segs[1]] = v2
        i += 1
    elif op == "sub":
        dict_reg[segs[1]] -= v2
        i += 1
    elif op == "mul":
        dict_reg[segs[1]] *= v2
        i += 1
        cnt += 1
    elif op == "jnz":
        if v1 != 0:
            i += v2
        else:
            i += 1
    else:
        raise Exception("Unrecognized op" + op)


print("Part 1:", cnt)


# Part 2.
import math
h = 0
# We tried creating some numbers to find the pattern.
# https://docs.google.com/spreadsheets/d/1aeoimBtBrZYvgiPvRbdPdOvWRuf3EUjjzWRUJMwq9qo/edit#gid=1061462023
for b in range(107900, 124901, 17):
    f = 1
    for d in range(2, math.isqrt(b) + 1):
        if b % d == 0:
            f = 0
            break
    if f == 0:
        h += 1

print("Part 2:", h)
