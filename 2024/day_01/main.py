import utils

filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

def parse_line(line):
    elements = line.split()
    return int(elements[0]), int(elements[1])

list_1 = []
list_2 = []
for line in lines:
    a, b = parse_line(line)
    list_1.append(a)
    list_2.append(b)


# Get the diffs.
diff = [abs(a - b) for a, b in zip(sorted(list_1), sorted(list_2))]

print("Part 1:", sum(diff))


# The lists are sorted now but it doesn't matter.
sim = 0
for num1 in list_1:
    num2 = len([n for n in list_2 if n == num1])
    sim += num1 * num2

print("Part 2:", sim)
