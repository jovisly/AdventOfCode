"""
Reflections: Part 1 - heapq again! Part 2 - can't do heapq anymore so dynamic programming.
"""
from functools import cache
from tqdm import tqdm
import heapq
import utils

filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().split("\n\n")
avail = lines[0].split(", ")
wants = lines[1].strip().split("\n")

# print(avail)
# print(wants)

def find_match(avail, want):
    queue = ([(len(want) - len(a), a) for a in avail if want.startswith(a)])
    while len(queue) > 0:
        cost, curr = heapq.heappop(queue)
        rest = want[len(curr):]
        options = [a for a in avail if rest.startswith(a)]
        for option in options:
            next = curr + option
            if next == want:
                return True
            else:
                queue.append((cost - len(option), curr + option))
    return False


n = 0
for want in tqdm(wants):
    if find_match(avail, want):
        n += 1

print("Part 1:", n)



@cache
def count_combos(want):
    if not want:
        return 1

    count = 0
    for a in avail:
        if want.startswith(a):
            count += count_combos(want[len(a):])
    return count


n = 0
for want in tqdm(wants):
    n_combos = count_combos(want)
    n += n_combos

print("Part 2:", n)


# THIS IS WAY TOO SLOW SAD SAD CRY CRY.
exit()
def find_all_combos(avail, want):
    queue = ([(len(want) - len(a), a) for a in avail if want.startswith(a)])
    combos = []
    while len(queue) > 0:
        cost, curr = heapq.heappop(queue)
        rest = want[len(curr):]
        options = [a for a in avail if rest.startswith(a)]
        for option in options:
            next = curr + option
            if next == want:
                combos.append(curr)
            else:
                queue.append((cost - len(option), curr + option))

    return len(combos)


n = 0
for want in tqdm(wants):
    n_combos = find_all_combos(avail, want)
    n += n_combos
    print(n_combos)



