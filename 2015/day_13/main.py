"""
Reflections: For part 1, on the first go I forgot to count the happiness score
between pairs, not just one way. I.e., (A, B) as well as (B, A).

I also took nearly the same approach as day 9 -- get all the permutations and
just iterate through.
"""
from itertools import permutations
from tqdm import tqdm

def parse_line(line):
    es = line.split(" ")
    p1 = es[0]
    p2 = es[-1][:-1]
    diff = int(es[3])
    if es[2] == "lose":
        diff = -1 * diff

    return p1, p2, diff


def get_all_people(lines):
    people = set()
    for line in lines:
        p1, p2, _ = parse_line(line)
        people.add(p1)
        people.add(p2)
    return list(people)


def get_dict_arrs(lines):
    dict_arrs = {}
    for line in lines:
        p1, p2, diff = parse_line(line)
        dict_arrs[(p1, p2)] = diff
    return dict_arrs


def get_total_diff(arr, dict_arrs):
    tot = 0
    for i, _ in enumerate(arr):
        if i == len(arr) - 1:
            j = 0
        else:
            j = i + 1
        diff = dict_arrs[(arr[j], arr[i])]
        tot += diff

        diff = dict_arrs[(arr[i], arr[j])]
        tot += diff
    return tot


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    dict_arrs = get_dict_arrs(lines)
    ps = get_all_people(lines)
    all_arrs = permutations(ps)
    max_val = 0
    for arr in tqdm(all_arrs):
        val = get_total_diff(arr, dict_arrs)
        if val > max_val:
            max_val = val

    print("Part 1:", max_val)

    # Add me to the dictionary.
    for p in ps:
        dict_arrs[("Me", p)] = 0
        dict_arrs[(p, "Me")] = 0

    ps.append("Me")
    all_arrs = permutations(ps)
    max_val = 0
    for arr in tqdm(all_arrs):
        val = get_total_diff(arr, dict_arrs)
        if val > max_val:
            max_val = val

    print("Part 2:", max_val)



if __name__ == "__main__":
    filename = "input.txt"
    solve(filename)


