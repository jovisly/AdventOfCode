import collections

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


def get_new_s(this, prev, next):
    """"Determine which new symbol S should be represented."""
    x, y = this[0], this[1]

    if( (x, y-1) == prev and (x, y+1) == next) or ( (x, y+1) == prev and (x, y-1) == next):
        return "|"

    if ((x-1, y) == prev and (x+1, y) == next) or ((x+1, y) == prev and (x-1, y) == next):
        return "-"

    if ((x, y-1) == prev and (x+1, y) == next) or ((x+1, y) == prev and (x, y-1) == next):
        return "L"

    if ((x-1, y) == prev and (x, y+1) == next) or ((x, y+1) == prev and (x-1, y) == next):
        return "7"

    if ((x, y-1) == prev and (x-1, y) == next) or ((x-1, y) == prev and (x, y-1) == next):
        return "J"

    if ((x+1, y) == prev and (x, y+1) == next) or ((x, y+1) == prev and (x+1, y) == next):
        return "F"

    print("Error: No new S found")
    return "X"


def get_num_steps(start, search_point, dict_map):
    this_point = start
    next_point = search_point
    num_steps = 0
    path = [this_point, next_point]
    new_s = "S"
    while True:
        dict_portal = dict_map[next_point]
        if this_point not in dict_portal:

            if num_steps == 0:
                return new_s, [], num_steps
            else:
                # This distance the full loop, so we add 1 for the starting
                # point, then divided by 2 for max distance.
                new_s = get_new_s(path[0], path[-2], path[1])
                return new_s, path[:-1], (num_steps + 1) / 2
        else:
            num_steps += 1
            dest = dict_portal[this_point]
            path.append(dest)
            this_point = next_point
            next_point = dest



def get_path(lines):
    """Returns the list of nodes that form the loop path."""
    dict_map = get_dict_map(lines)
    start = get_starting_position(lines)
    search_points = get_all_search_points(lines)
    max_path = []
    max_steps = 0
    new_s = "S"

    for search_point in search_points:
        new_s, path, num_steps = get_num_steps(start, search_point, dict_map)
        if num_steps > max_steps:
            max_steps = num_steps
            max_path = path

    return new_s, max_path



def get_cleaned_map(lines, path, new_s):
    """Remove symbols not in the path."""
    cleaned_map = []
    for y, line in enumerate(lines):
        new_line = []
        for x, symbol in enumerate(line):
            if (x, y) in path:
                if symbol == "S":
                    new_line.append(new_s)
                else:
                    new_line.append(symbol)
            else:
                new_line.append("*")
        cleaned_map.append("".join(new_line))
    return cleaned_map


def is_inside(line, pos):
    """Determine if a position is inside by counting borders to the left.

    A border can be |, or a pair of L and 7. If the number of borders is odd,
    then the position is inside. Otherwise, it's outside. Also the pairs F and J
    can work as a border.
    """
    counts = collections.Counter(list(line[:pos]))
    return (
        counts["|"] +
        min(counts["L"], counts["7"]) +
        min(counts["F"], counts["J"])
    ) % 2  == 1



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    new_s, path = get_path(lines)
    cleaned_map = get_cleaned_map(lines, path, new_s)
    # We can look at the entire map if we want.
    # for l in cleaned_map:
    #     print(l)
    num_inside = 0
    for y, line in enumerate(cleaned_map):
        for x, symbol in enumerate(line):
            if symbol == "*" and is_inside(line, x):
                # print("INSIDE: ", x, y)
                num_inside += 1

    return num_inside


def mini_test():
    filename = "input-test1.txt"
    assert solve(filename) == 1

    filename = "input-test2.txt"
    assert solve(filename) == 1

    filename = "input-test3.txt"
    assert solve(filename) == 1

    filename = "input-test4.txt"
    assert solve(filename) == 4

    filename = "input-test5.txt"
    assert solve(filename) == 4

    filename = "input-test6.txt"
    assert solve(filename) == 8

    filename = "input-test7.txt"
    assert solve(filename) == 10




if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
