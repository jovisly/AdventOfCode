"""
Bug report: Part 1 -- Ooof did not notice there are multiple lines. Part 2 -- even
worse. (a) Didn't realize it's a new test data, (b) had something that worked for
test data but not for the actual data, (c) tried something else but still it worked
for test data and failed for the actual data, (d) going mildly mad, (e) dog needed to
go out, (f) maybe it's supposed to be treated as one big line? And that was it.
"""
import re
import utils

filename = "input.txt"
# filename = "input-test.txt"
# filename = "input-test2.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

# Use regex to identify parts of the string that looks like "mul(2,4)"
mul_pattern = re.compile(r"mul\(([0-9]+),([0-9]+)\)")

def process_line_part1(line):
    res = 0
    for match in mul_pattern.finditer(line):
        n1 = int(match.group(1))
        n2 = int(match.group(2))
        res += n1 * n2
    return res

res = 0
for line in lines:
    res += process_line_part1(line)

print("Part 1:", res)


def get_should_enable(closest_do, closest_dont):
    if closest_do == -1 and closest_dont == -1:
        return True
    # If one of them is -1, then the other one decides.
    if closest_do == -1:
        return False
    if closest_dont == -1:
        return True
    # If both are not -1, then the closest (larger) one decides.
    if closest_do < closest_dont:
        return False
    else:
        return True


def process_line(line):
    res = 0
    for match in mul_pattern.finditer(line):
        start_index = match.start()
        n1 = int(match.group(1))
        n2 = int(match.group(2))
        temp_str = line[:start_index]
        # Find the last "do()" in the temp_str by string search.
        last_do = temp_str.rfind("do()")
        last_dont = temp_str.rfind("don't()")

        if get_should_enable(last_do, last_dont):
            res += n1 * n2
    return res


big_line = "".join(lines)
r = process_line(big_line)

print("Part 2:", r)
