import ast
from curses import wrapper
from viz import render_rocks

VIZ = True


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


def solve(filename, stdscr):
    lines = open(filename, encoding="utf-8").read().splitlines()
    rocks = [parse_line(l) for l in lines]
    filled_rocks = [fill_rocks(r) for r in rocks]

    if VIZ:
        render_rocks(stdscr, filled_rocks, num_sand=0)

    return 0



def main(stdscr):

    filename = "input-test.txt"
    solve(filename, stdscr)

    # print(total)
    stdscr.getch()


wrapper(main)
