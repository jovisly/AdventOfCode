import utils

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

def parse_line(line):
    parts = line.split(" ")
    range_parts = parts[0].split("-")
    min_val = int(range_parts[0])
    max_val = int(range_parts[1])
    letter = parts[1].split(":")[0]
    password = parts[-1]

    # Count number of times letter is in password.
    letters = [p for p in password]
    count = len([l for l in letters if l == letter])
    return min_val, max_val, count

res = 0
for line in lines:
    min_val, max_val, count = parse_line(line)
    if count <= max_val and count >= min_val:
      res += 1

print("Part 1:", res)


def parse_line_part2(line):
    parts = line.split(" ")
    range_parts = parts[0].split("-")
    pos1 = int(range_parts[0]) - 1
    pos2 = int(range_parts[1]) - 1
    letter = parts[1].split(":")[0]
    password = parts[-1]

    l1 = int(password[pos1] == letter)
    l2 = int(password[pos2] == letter)

    return int(l1 + l2 == 1)


res = 0
for line in lines:
    res += parse_line_part2(line)

print("Part 2:", res)
