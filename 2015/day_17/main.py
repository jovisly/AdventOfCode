"""
Reflections: python's intertools is seriously awesome.
"""
from itertools import combinations

def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    lines = [int(l) for l in lines]

    # Just iterate through all possibilities I guess.
    num_ways = 0
    min_num_containers = None
    for n in range(2, len(lines) + 1):
        comb = combinations(lines, n)
        for c in comb:
            if sum(list(c)) == 150:
                num_ways += 1

                if min_num_containers == None:
                    min_num_containers = n

    print("Part 1:", num_ways)

    comb = combinations(lines, min_num_containers)
    num_ways = 0
    for c in comb:
        if sum(list(c)) == 150:
            num_ways += 1
    print("Part 2:", num_ways)



if __name__ == "__main__":
    filename = "input.txt"
    solve(filename)


