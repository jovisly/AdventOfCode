import time
import curses
from utils import parse_line, fill_rocks
from viz import render_rocks, update_sand

VIZ = False

def move_sand(stdscr, x, y, new_pos, num):
    if VIZ:
        time.sleep(0.05)
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

    max_y = max([r[1] for r in all_rocks])
    if VIZ:
        render_rocks(stdscr, filled_rocks, max_y)

    all_sands = set()
    # Add "rocks" that are floors to all_rocks. Doesn't have to be precise.
    len_floor = 2 * (max_y + 6)
    for x in range(500 - len_floor // 2, 500 + len_floor // 2):
        all_rocks.add((x, max_y + 2))

    while True:
        sand_pos = make_one_sand(stdscr, all_rocks, all_sands, max_y + 2)
        if sand_pos is None:
            break
        all_sands.add(sand_pos)
        print(len(all_sands))

    return len(all_sands)


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
