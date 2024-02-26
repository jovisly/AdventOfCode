filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

line = lines[0]
digits = list(line)

tot = 0
for i, di in enumerate(digits):
    if i == len(digits) - 1:
        j = 0
    else:
        j = i + 1

    dj = digits[j]
    if di == dj:
        tot += int(di)

print("Part 1 tot:", tot)


tot = 0
for i, di in enumerate(digits):
    j = (i + len(digits) // 2) % len(digits)
    dj = digits[j]
    if di == dj:
        tot += int(di)

print("Part 2 tot:", tot)
