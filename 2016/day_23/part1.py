from collections import defaultdict

def do_cpy(inst, dict_reg, i):
    reg = inst.split(" ")[-1]
    if reg.replace("-", "").isdigit():
        return dict_reg, i + 1
    v = inst.split(" ")[1]
    if v.replace("-", "").isdigit():
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
    if reg.replace("-", "").isdigit():
        v = int(reg)
    else:
        v = dict_reg[reg]

    if v != 0:
        reg2 = inst.split(" ")[-1]
        if reg2.replace("-", "").isdigit():
            v2 = int(reg2)
        else:
            v2 = dict_reg[reg2]
        i += v2
    else:
        i += 1
    return dict_reg, i


def get_tgl_index(inst, dict_reg, i):
    reg = inst.split(" ")[1]
    v = dict_reg[reg]
    return i + v

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

dict_reg = defaultdict(int)
dict_reg["a"] = 7

i = 0
while i < len(lines):
    orig_i = i
    orig_line = lines[i]
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
    elif op == "tgl":
        tgl_ind = get_tgl_index(inst, dict_reg, i)
        i += 1
        if tgl_ind != i and tgl_ind < len(lines):
            orig_inst = lines[tgl_ind]
            op = orig_inst.split(" ")[0]
            if op == "cpy":
                # cpy becomes jnz.
                new_inst = orig_inst.replace("cpy", "jnz")
            elif op == "inc":
                # inc becomes dec
                new_inst = orig_inst.replace("inc", "dec")
            elif op == "dec":
                # dec becomes inc
                new_inst = orig_inst.replace("dec", "inc")
            elif op == "jnz":
                # jnz becomes cpy
                new_inst = orig_inst.replace("jnz", "cpy")
            elif op == "tgl":
                # tgl is one argument so also become inc
                new_inst = orig_inst.replace("tgl", "inc")
            else:
                raise ValueError(f"Unknown operation: {op}")

            lines[tgl_ind] = new_inst
    else:
        raise ValueError(f"Unknown operation: {op}")

    # if orig_i == 16:
    #     print("i:", orig_i, orig_line, "|", dict_reg)
    # input()


print(dict_reg["a"])
