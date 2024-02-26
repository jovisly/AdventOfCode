filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()
lines = [int(l) for l in lines]


i = 0
num_steps = 0
while i < len(lines):
    v = lines[i]
    lines[i] += 1
    i += v
    num_steps += 1


print("Part 1:", num_steps)


# Need to reset the values. Forgot this originally and couldn't match test answer.
filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()
lines = [int(l) for l in lines]


i = 0
num_steps = 0
while i < len(lines):
    v = lines[i]
    if v >= 3:
        lines[i] -= 1
    else:
        lines[i] += 1
    i += v
    num_steps += 1


print("Part 2:", num_steps)
