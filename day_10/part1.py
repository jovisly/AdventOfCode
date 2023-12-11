
def get_dict_portal_for_symbol(symbol, x, y):
    """Given a simple, get the portal dictionary for that position.

    For example, an "L" at position x and y will connect (x, y-1) and (x+1, y),
    so we return a dictionary of {(x, y-1): (x+1, y), (x+1, y): (x, y-1)} for
    the two-way mapping.
    """
    if symbol == ".":
        return {}
    elif symbol == "|":
        return {(x, y-1): (x, y+1), (x, y+1): (x, y-1)}
    elif symbol == "-":
        return {(x-1, y): (x+1, y), (x+1, y): (x-1, y)}
    elif symbol == "L":
        return {(x, y-1): (x+1, y), (x+1, y): (x, y-1)}
    elif symbol == "7":
        return {(x-1, y): (x, y+1), (x, y+1): (x-1, y)}
    elif symbol == "J":
        return {(x, y-1): (x-1, y), (x-1, y): (x, y-1)}
    elif symbol == "F":
        return {(x+1, y): (x, y+1), (x, y+1): (x+1, y)}
    elif symbol == "S":
        # This is our starting point!
        return {}
    else:
        print("Error: Unknown symbol", symbol)


def get_dict_map(lines):
    """Returns a dictionary that maps (x, y) to its portal dictionary."""
    dict_map = {}
    for y, line in enumerate(lines):
        for x, symbol in enumerate(line):
            dict_map[(x, y)] = get_dict_portal_for_symbol(symbol, x, y)
    return dict_map


def get_starting_position(lines):
    for y, line in enumerate(lines):
        for x, symbol in enumerate(line):
            if symbol == "S":
                return (x, y)


def get_all_search_points(lines):
    """Returns a list of all the search points."""
    x, y = get_starting_position(lines)
    max_x = len(lines[0])
    max_y = len(lines)
    search_points = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]

    return [
        p for p in search_points if 0 <= p[0] < max_x and 0 <= p[1] < max_y
    ]


def get_num_steps(start, search_point, dict_map):
    this_point = start
    next_point = search_point
    num_steps = 0
    while True:
        dict_portal = dict_map[next_point]
        if this_point not in dict_portal:

            if num_steps == 0:
                return num_steps
            else:
                # This distance the full loop, so we add 1 for the starting
                # point, then divided by 2 for max distance.
                return (num_steps + 1) / 2
        else:
            num_steps += 1
            dest = dict_portal[this_point]
            this_point = next_point
            next_point = dest


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    dict_map = get_dict_map(lines)

    start = get_starting_position(lines)
    search_points = get_all_search_points(lines)

    return max([
        get_num_steps(start, search_point, dict_map)
        for search_point in search_points
    ])


def mini_test():
    filename = "input-test1.txt"
    assert solve(filename) == 4

    filename = "input-test2.txt"
    assert solve(filename) == 8


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
