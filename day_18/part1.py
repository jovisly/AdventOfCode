
def map_dir(dir):
    if dir == "R":
        return (0, 1)
    elif dir == "L":
        return (0, -1)
    elif dir == "U":
        return (-1, 0)
    elif dir == "D":
        return (1, 0)
    else:
        raise ValueError(f"Unknown direction: {dir}")


def dig_edges(curr_pos, instruction):
    dir = map_dir(instruction[0])
    num_steps = int(instruction[1])
    return [
        (curr_pos[0] + (i + 1) * dir[0], curr_pos[1] + (i + 1) * dir[1])
        for i in range(num_steps)
    ]


def collapse_row(row):
    """Given, e.g., '###..##..#.#', returns '#.#.#.#.'."""
    collapsed = ""
    for c in list(row):
        if collapsed == "":
            collapsed += c
        else:
            if collapsed[-1] != c:
                collapsed += c

    return collapsed


def make_map(edges, visualize=True):
    num_cols = max([edge[1] for edge in edges]) + 1
    num_rows = max([edge[0] for edge in edges]) + 1
    dict_map = {}
    for row in range(num_rows):
        for col in range(num_cols):
            if (row, col) in edges:
                dict_map[(row, col)] = "#"
            else:
                dict_map[(row, col)] = "."

    # Fill the map and count number of grids within the pool (including edge).
    num_grids = 0
    for row in range(num_rows):
        for col in range(num_cols):
            if dict_map[(row, col)] == "#":
                num_grids += 1
            else:
                curr_row = "".join([dict_map[(row, col)] for col in range(col)])
                collapsed_row = collapse_row(curr_row)
                num_edges = collapsed_row.count("#")
                if num_edges % 2 == 1:
                    dict_map[(row, col)] = "o"
                    num_grids += 1

    if visualize:
        for row in range(num_rows):
            curr_row = "".join([dict_map[(row, col)] for col in range(num_cols)])
            print(f"{curr_row}")

    return num_grids, dict_map



def process_line(line):
    components = line.split(" ")
    return components[0], int(components[1])


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    lines = [process_line(line) for line in lines]

    edges = []
    curr_pos = (0,0)
    for line in lines:
        positions = dig_edges(curr_pos, line)
        curr_pos = positions[-1]
        edges += positions

    num_grids, _ = make_map(edges)
    return num_grids


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 62


if __name__ == "__main__":
    mini_test()

    # filename = "input.txt"
    # total = solve(filename)

    # print(total)
    # 22619 is not right which is obvious after we visualize the map.
    # 21321 is also not right, obviously.
