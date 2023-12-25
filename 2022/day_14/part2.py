import time
import curses
from utils import parse_line, fill_rocks
from viz import render_rocks, update_sand

VIZ = True

def move_sand(stdscr, x, y, new_pos, num):
    if VIZ:
        time.sleep(0.001)
        update_sand(stdscr, (x, y), new_pos, num)
    return new_pos


def make_one_sand(stdscr, all_rocks, all_sands, max_y):
    x, y = (500, 0)
    num = len(all_sands)

    while True:
        d = (x, y + 1)
        dl = (x - 1, y + 1)
        dr = (x + 1, y + 1)
        if d not in all_rocks and d not in all_sands:
            # Move down.
            if d[1] < max_y:
                x, y = move_sand(stdscr, x, y, d, num)
            else:
                return None
        elif dl not in all_rocks and dl not in all_sands:
            # Move down left.
            if dl[1] < max_y:
                x, y = move_sand(stdscr, x, y, dl, num)
            else:
                return None
        elif dr not in all_rocks and dr not in all_sands and dr[1] < max_y:
            # Move down right.
            if dr[1] < max_y:
                x, y = move_sand(stdscr, x, y, dr, num)
            else:
                return None
        else:
            # Stuck.
            return (x, y)


def solve(filename, stdscr):
    lines = open(filename, encoding="utf-8").read().splitlines()
    rocks = [parse_line(l) for l in lines]
    filled_rocks = [fill_rocks(r) for r in rocks]

    all_rocks = set()
    for r in filled_rocks:
        for pos in r:
            all_rocks.add(pos)

    if VIZ:
        render_rocks(stdscr, filled_rocks)


    return 0


def main(stdscr):
    stdscr.scrollok(True)

    curses.start_color()
    # Rock
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    # Sand
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    filename = "input-test.txt"
    solve(filename, stdscr)

    # print(total)
    stdscr.getch()



if VIZ:
    curses.wrapper(main)
else:
    pass
    filename = "input.txt"
    out = solve(filename, stdscr=None)
    print(out)
