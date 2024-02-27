from collections import defaultdict

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

dict_reg = defaultdict(int)

def perform_op(line):
    segs = line.split(" ")
    val = int(segs[-1])
    op = segs[-2]
    reg = segs[-3]

    # ops to support ['>=', '<', '<=', '!=', '>', '==']
    if (
        (op == ">=" and dict_reg[reg] >= val) or
        (op == "<" and dict_reg[reg] < val) or
        (op == "<=" and dict_reg[reg] <= val) or
        (op == "!=" and dict_reg[reg] != val) or
        (op == ">" and dict_reg[reg] > val) or
        (op == "==" and dict_reg[reg] == val)
    ):
        if segs[1] == "inc":
            dict_reg[segs[0]] += int(segs[2])
        else:
            dict_reg[segs[0]] -= int(segs[2])
    return dict_reg[segs[0]]


for line in lines:
    perform_op(line)


# Check what are the operations we need to support
# ops = [line.split(" ")[-2] for line in lines]
# ops = list(set(ops))
# print("Possible ops:", ops)

# We quickly verified that in "x op c", x is always symbolic and c is always int.
# compared = [line.split(" ")[-1] for line in lines]
# compared = [int(c) for c in compared]
# print(compared)

print("Part 1:", max(dict_reg.values()))


# Reset for part 2.
dict_reg = defaultdict(int)
max_v = 0
for line in lines:
    v = perform_op(line)
    if v > max_v:
        max_v = v

print("Part 2:", max_v)
