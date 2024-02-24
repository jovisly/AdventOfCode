"""
Not too bad; a lot of code to re-use from day 12. "Memorable" days for 2016
(i.e, the most challenging):

* Day 11: Of course; I still need to finish it.

* Day 22: Although could've been better if one visualizes it before jumping into
search algo like I did.

* Day 23: Part 1 just took a long time to implement all the logics correctly.
And Part 2 also took time to find the pattern.

A lot of code but not as difficult: Day 8 (I had a really bad bug), Day 9 (tried
several methods), Day 20 (took me some time to construct all the boundaries
correctly), Day 21 (simply a lot of operations to code and part2 was vague), Day
24 (could've been more difficult but similar to https://adventofcode.com/2022/day/16
so that experience, that much much more traumatic experience, really helped).

Well, now gotta go do Day 11 and move some radioactive stuff up and down the
elevator...
"""
from collections import defaultdict

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()


def try_an_int(initial_value):
    print("init:", initial_value)
    n_match = 100
    dict_reg = defaultdict(int)
    dict_reg["a"] = initial_value

    outputs = []
    i = 0
    while len(outputs) < n_match:
        inst = lines[i]

        op = inst.split(" ")[0]
        if op == "cpy":
            reg = inst.split(" ")[-1]
            v = inst.split(" ")[1]
            if v.isdigit():
                v = int(v)
            else:
                v = dict_reg[v]
            dict_reg[reg] = v
            i += 1
        elif op == "inc":
            reg = inst.split(" ")[-1]
            dict_reg[reg] += 1
            i += 1
        elif op == "dec":
            reg = inst.split(" ")[-1]
            dict_reg[reg] -= 1
            i += 1
        elif op == "jnz":
            reg = inst.split(" ")[1]
            if reg.isdigit():
                v = int(reg)
            else:
                v = dict_reg[reg]

            if v != 0:
                jump = int(inst.split(" ")[-1])
                i += jump
            else:
                i += 1
        elif op == "out":
            # It's only used for b.
            reg = inst.split(" ")[1]
            outputs.append(dict_reg[reg])
            i += 1
        else:
            raise ValueError(f"Unknown op: {op}")

    print("outputs:", outputs)
    ans = [0, 1] * (n_match // 2)
    if outputs == ans:
        return True
    else:
        return False



v = 0
while True:
    v += 1
    res = try_an_int(v)
    if res:
        print(v)
        exit()
