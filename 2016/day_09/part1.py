import utils



def get_inst(str, ind):
    """str[ind] is ( -- get the rest of the instruction."""
    # find the first closing bracket.
    ind_close = [i for i, c in enumerate(list(str)) if c == ")" and i > ind][0]
    inst_raw = str[ind:ind_close + 1]
    length_inst = len(inst_raw)
    # We actually don't want first and last char.
    inst_raw = inst_raw[1:-1]
    inst = inst_raw.split("x")
    inst = [int(i) for i in inst]
    return length_inst, inst[0], inst[1]


def decomp(str):
    res = ""
    i = 0
    while i < len(str):
        if str[i] == "(":
            # Going into () mode.
            length_inst, length_data, reps = get_inst(str, i)
            # print("length_inst, length_data, reps", length_inst, length_data, reps)
            data = str[i + length_inst:i + length_inst + length_data]
            for _ in range(reps):
                res += data

            # Go to the next position.
            i = i + length_inst + length_data
        else:
            res += str[i]
            i += 1

    # print(res)
    return res


assert decomp("ADVENT") == "ADVENT"
assert decomp("A(1x5)BC") == "ABBBBBC"
assert decomp("(3x3)XYZ") == "XYZXYZXYZ"
assert decomp("A(2x2)BCD(2x2)EFG") == "ABCBCDEFEFG"
assert decomp("(6x1)(1x3)A") == "(1x3)A"
assert decomp("X(8x2)(3x3)ABCY") == "X(3x3)ABC(3x3)ABCY"


filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()
line = lines[0]

out = decomp(line)
print(len(line))
print(len(out))
