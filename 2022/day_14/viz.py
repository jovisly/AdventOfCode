X_OFFSET = 486
Y_OFFSET = 4


def render_rocks(stdscr, rocks, num_sand, min_x=490, max_x=505, min_y=0, max_y=10):
    stdscr.clear()

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            stdscr.addstr(y + Y_OFFSET, x - X_OFFSET, ".")

    # Add sand starting position.
    x, y = (500, 0)
    stdscr.addstr(y + Y_OFFSET, x - X_OFFSET, "+")


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
