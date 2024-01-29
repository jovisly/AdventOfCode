"""
Reflections: Wasted some time trying to come up with all possible ways of
dividing the list into three groups. This would take too long to iterate. Then
realized that we know what the goal weight is, and we really only care about one
group. That worked out much faster and easier, and also is directly applicable
for part 2.
"""
import math
from itertools import combinations
from tqdm import tqdm


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    nums = [int(l) for l in lines]
    goal_sum = sum(nums) / 3
    print("Goal sum:", goal_sum)

    # All we need to do is pick one group that sum up to s / 3, and check for
    # the group that has the lowest number of items, and, if there are multiple,
    # pick for the lowest product.
    num_items = 0
    while True:
        num_items += 1
        candidates = []
        combs = list(combinations(nums, num_items))
        for comb in combs:
            if sum(comb) == goal_sum:
                candidates.append(comb)

        if len(candidates) > 0:
            break

    # Now pick the candidates with the minimum product.
    min_prod = None
    for c in candidates:
        p = math.prod(c)
        if min_prod is None or p < min_prod:
            min_prod = p

    print("Part 1:", min_prod)

    # Part 2: Basically repeat part 1 but goal sum is divided by 4 instead.
    goal_sum = sum(nums) / 4
    print("Goal sum:", goal_sum)

    num_items = 0
    while True:
        num_items += 1
        candidates = []
        combs = list(combinations(nums, num_items))
        for comb in combs:
            if sum(comb) == goal_sum:
                candidates.append(comb)

        if len(candidates) > 0:
            break

    min_prod = None
    for c in candidates:
        p = math.prod(c)
        if min_prod is None or p < min_prod:
            min_prod = p
    print("Part 2:", min_prod)



if __name__ == "__main__":
    filename = "input.txt"
    solve(filename)


