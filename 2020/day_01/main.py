import utils

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()


for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        if int(lines[i]) + int(lines[j]) == 2020:
            out = int(lines[i]) * int(lines[j])

print("Part 1:", out)

for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        for k in range(j+1, len(lines)):
            if int(lines[i]) + int(lines[j]) + int(lines[k]) == 2020:
                out = int(lines[i]) * int(lines[j]) * int(lines[k])

print("Part 2:", out)
