from collections import defaultdict
import utils

part2 = True

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

dict_reg = defaultdict(int)
if part2:
    dict_reg["c"] = 1

i = 0
while i < len(lines):
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
    else:
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

print(dict_reg["a"])
