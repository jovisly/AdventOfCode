import curses

# For test dataset.
X_OFFSET = 476
Y_OFFSET = 4

MIN_X = 480
MAX_X = 516
MIN_Y = -1
MAX_Y = 12

# For real dataset.
# X_OFFSET = 407
# Y_OFFSET = 0

# MIN_X = 409
# MAX_X = 518
# MIN_Y = 0
# MAX_Y = 170


def render_rocks(stdscr, rocks, rocks_max_y, min_x=MIN_X, max_x=MAX_X, min_y=MIN_Y, max_y=MAX_Y):
    stdscr.clear()
    screen_y, screen_x = stdscr.getmaxyx()

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if y + Y_OFFSET >= screen_y:
                continue
            if x - X_OFFSET >= screen_x:
                continue
            stdscr.addstr(y + Y_OFFSET, x - X_OFFSET, ".")

    # Add rocks.
    for r in rocks:
        for pos in r:
            x, y = pos
            if y + Y_OFFSET >= screen_y:
                continue
            if x - X_OFFSET >= screen_x:
                continue
            stdscr.addstr(y + Y_OFFSET, x - X_OFFSET, "#", curses.color_pair(1) | curses.A_BOLD)

    # Add floor. Only relevant for part 2.
    for x in range(min_x, max_x + 1):
        y = rocks_max_y + 2
        if y + Y_OFFSET >= screen_y:
            continue
        if x - X_OFFSET >= screen_x:
            continue
        stdscr.addstr(y + Y_OFFSET, x - X_OFFSET, "#", curses.color_pair(1) | curses.A_BOLD)


    stdscr.refresh()


def update_sand(stdscr, old_pos, new_pos, num_sand, min_x=MIN_X, max_x=MAX_X, min_y=MIN_Y, max_y=MAX_Y):
    screen_y, screen_x = stdscr.getmaxyx()

    # Old Pos should revert to empty.
    x, y = old_pos
    if y + Y_OFFSET >= screen_y:
        return
    if x - X_OFFSET >= screen_x:
        return

    stdscr.addstr(y + Y_OFFSET, x - X_OFFSET, ".")
    # New Pos should be a sand.
    x, y = new_pos
    stdscr.addstr(y + Y_OFFSET, x - X_OFFSET, "O", curses.color_pair(2) | curses.A_BOLD)

    # stdscr.addstr(
    #     screen_y // 4,
    #     max_x - X_OFFSET + 2,
    #     f"Num sand: {num_sand}"
    # )
    stdscr.addstr(
        max_y + Y_OFFSET + 2,
        min_x - X_OFFSET + 0,
        f"Num sand: {num_sand}"
    )
    stdscr.refresh()


