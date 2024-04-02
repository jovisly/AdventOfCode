from collections import defaultdict

cnts = defaultdict(int)

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

for line in lines:
    x0y0 = line.split(": ")[0].split(" @ ")[1]
    x0 = int(x0y0.split(",")[0])
    y0 = int(x0y0.split(",")[1])

    dxdy = line.split(": ")[1]
    dx = int(dxdy.split("x")[0])
    dy = int(dxdy.split("x")[1])

    for x in range(x0, x0 + dx):
        for y in range(y0, y0 + dy):
            cnts[(x, y)] += 1


print("Part 1:", len([v for v in cnts.values() if v >= 2]))


# At this point we have cnts. We will go through the lines again and see if
# there is any line where the dict values are all 1's.

for line in lines:
    id = line.split(": ")[0].split(" @ ")[0][1:]
    x0y0 = line.split(": ")[0].split(" @ ")[1]
    x0 = int(x0y0.split(",")[0])
    y0 = int(x0y0.split(",")[1])

    dxdy = line.split(": ")[1]
    dx = int(dxdy.split("x")[0])
    dy = int(dxdy.split("x")[1])

    num_1 = 0
    num_tot = 0
    for x in range(x0, x0 + dx):
        for y in range(y0, y0 + dy):
            if cnts[(x, y)] == 1:
                num_1 += 1
            num_tot += 1
    if num_1 == num_tot:
        print("Part 2:", id)


