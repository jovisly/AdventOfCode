import ast
import time
from curses import wrapper
from viz import render_rocks, update_sand

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



def move_sand(stdscr, x, y, new_pos):
    if VIZ:
        time.sleep(0.1)
        update_sand(stdscr, (x, y), new_pos)
    return new_pos



def make_one_sand(stdscr, all_rocks, all_sands, max_y):
    x, y = (500, 0)
    stuck = False

    while stuck is False:
        d = (x, y + 1)
        dl = (x - 1, y + 1)
        dr = (x + 1, y + 1)
        if d not in all_rocks and d not in all_sands and d[1] <= max_y:
            # Move down.
            x, y = move_sand(stdscr, x, y, d)
        elif dl not in all_rocks and dl not in all_sands and dl[1] <= max_y:
            # Move down left.
            x, y = move_sand(stdscr, x, y, dl)
        elif dr not in all_rocks and dr not in all_sands and dr[1] <= max_y:
            # Move down right.
            x, y = move_sand(stdscr, x, y, dr)
        else:
            # Stuck.
            stuck = True


    # Only return the sand position if it can stay on the map.
    return (x, y) if y < max_y else None



def solve(filename, stdscr):
    lines = open(filename, encoding="utf-8").read().splitlines()
    rocks = [parse_line(l) for l in lines]
    filled_rocks = [fill_rocks(r) for r in rocks]

    # filled rocks is a list of lists of tuples. We will flatten it to a list of
    # tuples so that we can turn it into a set for faster membership check.
    all_rocks = set()
    for r in filled_rocks:
        for pos in r:
            all_rocks.add(pos)

    if VIZ:
        render_rocks(stdscr, filled_rocks, num_sand=0)

    # No point in keeping the sand if it goes below the lowest rock. Nothing to
    # catch it.
    max_y = max([r[1] for r in all_rocks])
    all_sands = set()
    sand_pos = make_one_sand(stdscr, all_rocks, all_sands, max_y)
    all_sands.add(sand_pos)
    sand_pos = make_one_sand(stdscr, all_rocks, all_sands, max_y)


    return 0



def main(stdscr):

    filename = "input-test.txt"
    solve(filename, stdscr)

    # print(total)
    stdscr.getch()


wrapper(main)
