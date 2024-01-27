"""Reflections: Oh hey a classic game of life!"""
from utils import *
from tqdm import tqdm


def update_lights(dict_lights):
    new_dict_light = {}
    for k, v in dict_lights.items():
        neighbors_pos = get_neighbors(k, num_dirs=8)
        neighbors_pos = [
            p for p in neighbors_pos
            if p[0] >= 0 and p[0] < 100 and p[1] >= 0 and p[1] < 100
            # Membership check of dictionary key is slowing things down.
        ]
        num_neighbors_on = sum([dict_lights[p] for p in neighbors_pos])
        if v == 1:
            if num_neighbors_on == 2 or num_neighbors_on == 3:
                new_dict_light[k] = 1
            else:
                new_dict_light[k] = 0
        else:
            if num_neighbors_on == 3:
                new_dict_light[k] = 1
            else:
                new_dict_light[k] = 0
    return new_dict_light


def turn_on_corners(dict_lights):
    new_dict_light = {
        k: v for k, v in dict_lights.items()
    }
    new_dict_light[(0, 0)] = 1
    new_dict_light[(0, 99)] = 1
    new_dict_light[(99, 99)] = 1
    new_dict_light[(99, 0)] = 1
    return new_dict_light


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    dict_lights = get_dict_board(lines)

    for k, v in dict_lights.items():
        if v == "#":
            dict_lights[k] = 1
        else:
            dict_lights[k] = 0

    for _ in tqdm(range(100)):
        dict_lights = update_lights(dict_lights)

    print("Part 1:", sum(dict_lights.values()))

    # Part 2: Reset dict_lights.
    lines = open(filename, encoding="utf-8").read().splitlines()
    dict_lights = get_dict_board(lines)
    for k, v in dict_lights.items():
        if v == "#":
            dict_lights[k] = 1
        else:
            dict_lights[k] = 0
    dict_lights = turn_on_corners(dict_lights)

    for _ in tqdm(range(100)):
        dict_lights = update_lights(dict_lights)
        dict_lights = turn_on_corners(dict_lights)

    print("Part 2:", sum(dict_lights.values()))



if __name__ == "__main__":
    filename = "input.txt"
    solve(filename)


