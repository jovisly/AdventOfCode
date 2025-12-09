import utils

filename = "input.txt"
filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().splitlines()
list_pos = [tuple(int(p) for p in line.split(",")) for line in lines]

max_area = 0
for i in range(len(list_pos)):
    for j in range(len(list_pos)):
        if i == j:
            continue

        abs_x = abs(list_pos[i][0] - list_pos[j][0]) + 1
        abs_y = abs(list_pos[i][1] - list_pos[j][1]) + 1
        area = abs_x * abs_y
        if area > max_area:
            max_area = area

print("Part 1:", max_area)

print("Part 2:")
