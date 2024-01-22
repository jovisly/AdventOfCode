"""
Reflections: There must be more efficient algorithms but since the actual data
set contains not that many cities, so computing all permutations is not that bad
at all.
"""
from itertools import permutations
from tqdm import tqdm

def parse_line(line):
    es = line.split(" ")
    return es[0], es[2], int(es[-1])


def get_dict_paths(lines):
    dict_paths = {}
    for line in lines:
        c1, c2, dist = parse_line(line)
        dict_paths[(c1, c2)] = dist
        dict_paths[(c2, c1)] = dist
    return dict_paths


def get_all_cities(lines):
    cities = set()
    for line in lines:
        c1, c2, _ = parse_line(line)
        cities.add(c1)
        cities.add(c2)
    return list(cities)


def get_route_dist(dict_paths, route):
    tot = 0
    for i, c in enumerate(route):
        if i == 0:
            continue
        j = i - 1
        dist = dict_paths[(route[j], route[i])]
        tot += dist
    return tot


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    dict_paths = get_dict_paths(lines)
    cities = get_all_cities(lines)
    routes = permutations(cities)

    min_dist = 99999999999
    max_dist = -1
    for route in tqdm(routes):
        dist = get_route_dist(dict_paths, route)
        if dist < min_dist:
            min_dist = dist
        if dist > max_dist:
            max_dist = dist

    print("Part 1:", min_dist)
    print("Part 2:", max_dist)



if __name__ == "__main__":
    filename = "input.txt"
    solve(filename)


