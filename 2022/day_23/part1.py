"""
Time: 40 minutes

Reflections: Not too bad and another board question. Except this time also the
diagonal directions. I was a bit confused with the instruction which does not
specify what to do if there's no valid moves -- it was not explicitly stated that
do nothing in such case.
"""
import utils

all_dirs = ["E", "W", "N", "S", "NE", "NW", "SE", "SW"]

def map_dir(dir):
    if dir == "E":
        return (0, 1)
    elif dir == "W":
        return (0, -1)
    elif dir == "N":
        return (-1, 0)
    elif dir == "S":
        return (1, 0)
    elif dir == "NE":
        return (-1, 1)
    elif dir == "NW":
        return (-1, -1)
    elif dir == "SE":
        return (1, 1)
    elif dir == "SW":
        return (1, -1)
    else:
        raise ValueError(f"Unknown direction: {dir}")


def move_to_dir(pos, dir):
    mapped_dir = map_dir(dir)
    return (pos[0] + mapped_dir[0], pos[1] + mapped_dir[1])


def get_neighbors(pos, list_elves):
    return [d for d in all_dirs if move_to_dir(pos, d) in list_elves]



def propose_move(pos, list_elves, round_num):
    neighbors = get_neighbors(pos, list_elves)
    if len(neighbors) == 0:
        return None

    # Wait a minute why not get all possible moves first then shuffle based on
    # round num? Save that for part 2.
    if round_num % 4 == 0:
        ex = ["N", "NE", "NW"]
        if all(n not in ex for n in neighbors):
            return move_to_dir(pos, "N")

        ex = ["S", "SE", "SW"]
        if all(n not in ex for n in neighbors):
            return move_to_dir(pos, "S")

        ex = ["W", "NW", "SW"]
        if all(n not in ex for n in neighbors):
            return move_to_dir(pos, "W")

        ex = ["E", "NE", "SE"]
        if all(n not in ex for n in neighbors):
            return move_to_dir(pos, "E")
    elif round_num % 4 == 1:
        ex = ["S", "SE", "SW"]
        if all(n not in ex for n in neighbors):
            return move_to_dir(pos, "S")

        ex = ["W", "NW", "SW"]
        if all(n not in ex for n in neighbors):
            return move_to_dir(pos, "W")

        ex = ["E", "NE", "SE"]
        if all(n not in ex for n in neighbors):
            return move_to_dir(pos, "E")

        ex = ["N", "NE", "NW"]
        if all(n not in ex for n in neighbors):
            return move_to_dir(pos, "N")
    elif round_num % 4 == 2:
        ex = ["W", "NW", "SW"]
        if all(n not in ex for n in neighbors):
            return move_to_dir(pos, "W")

        ex = ["E", "NE", "SE"]
        if all(n not in ex for n in neighbors):
            return move_to_dir(pos, "E")

        ex = ["N", "NE", "NW"]
        if all(n not in ex for n in neighbors):
            return move_to_dir(pos, "N")
        ex = ["S", "SE", "SW"]
        if all(n not in ex for n in neighbors):
            return move_to_dir(pos, "S")
    else:
        ex = ["E", "NE", "SE"]
        if all(n not in ex for n in neighbors):
            return move_to_dir(pos, "E")

        ex = ["N", "NE", "NW"]
        if all(n not in ex for n in neighbors):
            return move_to_dir(pos, "N")
        ex = ["S", "SE", "SW"]
        if all(n not in ex for n in neighbors):
            return move_to_dir(pos, "S")

        ex = ["W", "NW", "SW"]
        if all(n not in ex for n in neighbors):
            return move_to_dir(pos, "W")

    # No valid move so we do nothing right?
    return None


def resolve_proposals(proposals):
    new_proposals = {}
    for k, v in proposals.items():
        if v is not None:
            others = [
                v2 for k2, v2 in proposals.items() if k2 != k
            ]
            if v not in others:
                new_proposals[k] = v
            else:
                new_proposals[k] = None
        else:
            new_proposals[k] = None

    return new_proposals


def update_elves(list_elves, proposals):
    new_list = []
    for e in list_elves:
        if proposals[e] is not None:
            new_list.append(proposals[e])
        else:
            new_list.append(e)
    return new_list


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()

    # Get coordinates of the elves.
    dict_elves = utils.get_dict_board(lines)
    list_elves = [
        k for k, v in dict_elves.items() if v == "#"
    ]

    for i in range(10):
        proposals = {pos: propose_move(pos, list_elves, i) for pos in list_elves}
        proposals = resolve_proposals(proposals)
        list_elves = update_elves(list_elves, proposals)

    # Then get the grid size and subtract elves.
    max_r = max([e[0] for e in list_elves])
    max_c = max([e[1] for e in list_elves])
    min_r = min([e[0] for e in list_elves])
    min_c = min([e[1] for e in list_elves])
    area = (max_r - min_r + 1) * (max_c - min_c + 1)

    return area - len(list_elves)


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 110


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
