from collections import Counter

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

num_2 = 0
num_3 = 0
for line in lines:
    cnt = Counter(line)
    values = cnt.values()
    if 2 in values:
        num_2 += 1
    if 3 in values:
        num_3 += 1

print("Part 1:", num_2 * num_3)


def diff_by_one(arr1, arr2):
    n = 0
    for a1, a2 in zip(arr1, arr2):
        if a1 != a2:
            n += 1
    if n == 1:
        return True
    else:
        return False


for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        if diff_by_one(lines[i], lines[j]):
            print(lines[i])
            print(lines[j])

