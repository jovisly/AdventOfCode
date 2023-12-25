import ast

def parse_line(line):
    line = line.split(" -> ")
    line = [ast.literal_eval(l) for l in line]
    return line


def fill_rocks(rock):
    """Given edges, fill up rock path.

    Should be okay to do since the map looks to be no more than 1000x1000.
    """
    new_rock = []
    for ind, this_edge in enumerate(rock):
        if ind == 0:
            # new_rock.append(this_edge)
            continue
        prev_edge = rock[ind - 1]
        if this_edge[0] == prev_edge[0]:
            # Vertical.
            min = prev_edge[1] if prev_edge[1] < this_edge[1] else this_edge[1]
            max = prev_edge[1] if prev_edge[1] > this_edge[1] else this_edge[1]
            for y in range(min, max + 1):
                new_rock.append((prev_edge[0], y))
        else:
            # Horizontal.
            min = prev_edge[0] if prev_edge[0] < this_edge[0] else this_edge[0]
            max = prev_edge[0] if prev_edge[0] > this_edge[0] else this_edge[0]
            for x in range(min, max + 1):
                new_rock.append((x, prev_edge[1]))
    return new_rock



def get_dimension(filename):
    # Get a sense how big the map is.
    lines = open(filename, encoding="utf-8").read().splitlines()
    rocks = [parse_line(l) for l in lines]
    filled_rocks = [fill_rocks(r) for r in rocks]

    all_rocks = set()
    for r in filled_rocks:
        for pos in r:
            all_rocks.add(pos)

    max_y = max([r[1] for r in all_rocks])
    min_y = min([r[1] for r in all_rocks])
    max_x = max([r[0] for r in all_rocks])
    min_x = min([r[0] for r in all_rocks])

    print(f"max_y: {max_y}")
    print(f"min_y: {min_y}")
    print(f"max_x: {max_x}")
    print(f"min_x: {min_x}")


if __name__ == "__main__":
    get_dimension("input-test.txt")
    print("#" * 80)
    get_dimension("input.txt")


