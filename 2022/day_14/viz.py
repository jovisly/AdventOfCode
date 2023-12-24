X_OFFSET = 486
Y_OFFSET = 4

MIN_X = 486
MAX_X = 505
MIN_Y = 0
MAX_Y = 10


def render_rocks(stdscr, rocks, num_sand, min_x=MIN_X, max_x=MAX_X, min_y=MIN_Y, max_y=MAX_Y):
    stdscr.clear()

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            stdscr.addstr(y + Y_OFFSET, x - X_OFFSET, ".")

    # Add rocks.
    for r in rocks:
        for pos in r:
            x, y = pos
            stdscr.addstr(y + Y_OFFSET, x - X_OFFSET, "#")


    # Denote how many sand.
    stdscr.addstr(
        max_y + Y_OFFSET + 2,
        min_x - X_OFFSET,
        f"Num sand: {num_sand}"
    )


    stdscr.refresh()


def update_sand(stdscr, old_pos, new_pos, min_x=MIN_X, max_x=MAX_X, min_y=MIN_Y, max_y=MAX_Y):
    # Old Pos should revert to empty.
    x, y = old_pos
    stdscr.addstr(y + Y_OFFSET, x - X_OFFSET, ".")
    # New Pos should be a sand.
    x, y = new_pos
    stdscr.addstr(y + Y_OFFSET, x - X_OFFSET, "o")

    # Move cursor out of the way.
    stdscr.addstr(
        max_y + Y_OFFSET + 2,
        min_x - X_OFFSET + 20,
        ""
    )

    stdscr.refresh()
