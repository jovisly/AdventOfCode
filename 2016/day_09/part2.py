"""
Reflections: Oof this took a while. First attempt to just count and not expand
the string got too buggy and gave up on that approach. Second attempt uses a
simpler method of tracking just the positions that should expand. Second method
was a lot better: easier to implement and didn't require crazy recursion.
"""
import utils

from part1 import decomp, get_inst

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

def really_decomp(str):
    while "(" in str:
        print("decomp...", len(str))
        str = decomp(str)
    return str


def get_ann(str):
    ann = []
    in_paren = False
    for c in list(str):
        if c == "(":
            in_paren = True
            ann.append(0)
        elif c == ")":
            in_paren = False
            ann.append(0)
        else:
            if in_paren:
                ann.append(0)
            else:
                ann.append(1)
    return ann



def just_count(str):
    # Step 1: create annotation. denote which part of the string should count.
    ann = get_ann(str)
    i = 0
    while i < len(str):
        if str[i] == "(":
            length_inst, length_data, reps = get_inst(str, i)
            for j in range(i + length_inst, i + length_inst + length_data):
                ann[j] = ann[j] * reps

            # Go to the next position.
            i = i + length_inst
        else:
            i += 1

    return sum(ann)



assert really_decomp("(3x3)XYZ") == "XYZXYZXYZ"
assert really_decomp("X(8x2)(3x3)ABCY") == "XABCABCABCABCABCABCY"
assert len(really_decomp("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN")) == 445
# This will take a few minutes. It'll probably be too slow for the actual data.
# assert len(really_decomp("(27x12)(20x12)(13x14)(7x10)(1x12)A")) == 241920

assert just_count("(3x3)XYZ") == len("XYZXYZXYZ")
assert just_count("X(8x2)(3x3)ABCY") == len("XABCABCABCABCABCABCY")
assert just_count("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN") == 445
assert just_count("(27x12)(20x12)(13x14)(7x10)(1x12)A") == 241920


filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()
line = lines[0]

out = just_count(line)
print(out)
exit()

# Too buggy; not going to use it.
def just_count(str):
    # Decomp but only returns resulting length.
    res = 0
    i = 0
    while i < len(str):
        if str[i] == "(":
            # Going into () mode.
            length_inst, length_data, reps = get_inst(str, i)
            length_data_orig = length_data
            data = str[i + length_inst:i + length_inst + length_data]
            print("reps:", reps)
            while data.startswith("("):
                sub_length_inst, length_data, sub_reps = get_inst(data, 0)
                data = data[sub_length_inst:]
                print("reps:", reps, "multiplied by", sub_reps, "equals = " , reps * sub_reps)

                reps *= sub_reps

            res += length_data * reps
            print("length of data:", length_data, "reps:", reps)
            # Go to the next position.
            i += length_inst + length_data_orig
        else:
            print("adding res 1:", str[i])

            res += 1
            i += 1

    print("res:", res)
    return res
