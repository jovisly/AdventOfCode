from collections import defaultdict

def do_cpy(inst, dict_reg, i):
    reg = inst.split(" ")[-1]
    v = inst.split(" ")[1]
    if v.isdigit():
        v = int(v)
    else:
        v = dict_reg[v]
    dict_reg[reg] = v

    return dict_reg, i + 1


def do_inc(inst, dict_reg, i):
    reg = inst.split(" ")[-1]
    dict_reg[reg] += 1
    return dict_reg, i + 1


def do_dec(inst, dict_reg, i):
    reg = inst.split(" ")[-1]
    dict_reg[reg] -= 1
    return dict_reg, i + 1


def do_jnz(inst, dict_reg, i):
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
    return dict_reg, i

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

dict_reg = defaultdict(int)

i = 0
while i < len(lines):
    inst = lines[i]

    op = inst.split(" ")[0]
    if op == "cpy":
        dict_reg, i = do_cpy(inst, dict_reg, i)
    elif op == "inc":
        dict_reg, i = do_inc(inst, dict_reg, i)
    elif op == "dec":
        dict_reg, i = do_dec(inst, dict_reg, i)
    elif op == "jnz":
        dict_reg, i = do_jnz(inst, dict_reg, i)
    else:
        raise ValueError(f"Unknown operation: {op}")


print(dict_reg["a"])
