from collections import Counter

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

v = 0
for line in lines:
    v += int(line)

print("Part 1:", v)

v = 0
d = Counter()
d[v] += 1
i = -1

while True:
    i += 1
    i = i % len(lines)
    line = lines[i]
    v += int(line)
    d[v] += 1
    if d[v] == 2:
        break

print("Part 2:", v)
