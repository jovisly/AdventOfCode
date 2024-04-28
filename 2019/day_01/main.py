import math

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

total = 0

for line in lines:
    total += int(int(line) / 3) - 2


print("Part 1:", total)


def get_fuel(input_str):
    i = int(int(input_str) / 3) - 2
    t = i if i > 0 else 0
    while i > 0:
        i = int(i / 3) - 2
        if i > 0:
            t += i
    return t

total = 0

for line in lines:
    total += get_fuel(line)


print("Part 2:", total)
