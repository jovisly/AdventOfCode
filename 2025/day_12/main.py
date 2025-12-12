"""Just tried to count by area which doesn't work with test as a what the heck.

That worked!?  Did I learn anything?
"""

filename = "input.txt"
# filename = "input-test.txt"
line = open(filename, encoding="utf-8").read()

parts = line.split("\n\n")
reqs = parts[-1]
blocks = parts[:-1]

def get_block_size(block):
    return len([char for char in block if char == "#"])

block_sizes = [get_block_size(block) for block in blocks]
print(block_sizes)

reqs = reqs.strip().splitlines()
def get_area(req):
    parts = req.split(":")
    dims = parts[0].split("x")
    return int(dims[0]) * int(dims[1])

def get_req_counts(req):
    parts = req.split(":")
    counts = parts[1].strip().split()
    return [int(count) for count in counts]

reqs_area = [get_area(req) for req in reqs]
print(reqs_area)

reqs_counts = [get_req_counts(req) for req in reqs]
print(reqs_counts)

num = 0
for area, counts in zip(reqs_area, reqs_counts):
    tot = sum(counts)
    if tot * 7 > area:
        print("impossible")
    else:
        print("possible")
        num += 1


print("Part 1:", num)
