# Problem type:
# ~~~~~~~~~~~~ (almost) freebie ~~~~~~~~~~~~
from collections import defaultdict

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

dd = defaultdict(list)

for line in lines:
    segs = line.split(" <-> ")
    parent = int(segs[0])
    children = segs[1].split(", ")
    children = [int(c) for c in children]
    prev = dd[parent]
    next = list(set(prev + children))
    dd[parent] = next


queue = [0]
visited = set()
while len(queue) > 0:
    q = queue.pop()
    children = dd[q]
    for c in children:
        if c not in visited:
            queue.append(c)
            visited.add(c)

print("Part 1:", len(visited))

# We want to get all groups. Let's abstract away the function.
def get_all_children(n):
    queue = [n]
    visited = set()
    while len(queue) > 0:
        q = queue.pop()
        children = dd[q]
        for c in children:
            if c not in visited:
                queue.append(c)
                visited.add(c)
    return list(visited)

all_children = []
n = 0
n_groups = 0
while len(all_children) != len(list(dd)):
    n_groups += 1
    children = get_all_children(n)
    all_children = list(set(all_children + children))
    excluded = [n for n in list(dd) if n not in all_children]
    if len(excluded) == 0:
        break
    else:
        n = excluded[0]


print("Part 2:", n_groups)
