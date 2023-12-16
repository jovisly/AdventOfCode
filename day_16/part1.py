
def map_dir(dir):
    if dir == "r":
        return (0, 1)
    elif dir == "l":
        return (0, -1)
    elif dir == "u":
        return (-1, 0)
    elif dir == "d":
        return (1, 0)
    else:
        raise ValueError(f"Unknown direction: {dir}")



def is_valid_pos(layout, pos):
    return (
        pos[0] >= 0 and pos[0] < len(layout)
        and pos[1] >= 0 and pos[1] < len(layout[0])
    )



def go_to_next(layout, ray):
    """Move the ray to the next position.

    Returns a list of rays, since a ray can split.
    """
    curr_pos = ray[0]
    cell = layout[curr_pos[0]][curr_pos[1]]
    dir = ray[1]

    # Scenario 1: Keep going.
    # We keep going if (a) encounter nothing, or (b) encounter | while going up
    # or down, or (c) encounter - while going left or right.
    if (
        cell == "." or
        (cell == "|" and dir in ["u", "d"]) or
        (cell == "-" and dir in ["l", "r"])
    ):
        mapped_dir = map_dir(dir)
        new_pos = (curr_pos[0] + mapped_dir[0], curr_pos[1] + mapped_dir[1])
        return {(new_pos, dir)}


    # Scenario 2: Splitting.
    if cell == "|":
        # Split -- one goes up and one goes down.
        pos_u = (curr_pos[0] - 1, curr_pos[1])
        pos_d = (curr_pos[0] + 1, curr_pos[1])
        return {
            (pos_u, "u"),
            (pos_d, "d"),
        }

    if cell == "-":
        # Split -- one goes left and one goes right.
        pos_l = (curr_pos[0], curr_pos[1] - 1)
        pos_r = (curr_pos[0], curr_pos[1] + 1)
        return {
            (pos_l, "l"),
            (pos_r, "r"),
        }


    # Scenario 3: Reflecting.
    if cell == "/":
        if dir == "u":
            new_dir = "r"
        if dir == "d":
            new_dir = "l"
        if dir == "l":
            new_dir = "d"
        if dir == "r":
            new_dir = "u"

    if cell == "\\":
        if dir == "u":
            new_dir = "l"
        if dir == "d":
            new_dir = "r"
        if dir == "l":
            new_dir = "u"
        if dir == "r":
            new_dir = "d"

    mapped_dir = map_dir(new_dir)
    new_pos = (curr_pos[0] + mapped_dir[0], curr_pos[1] + mapped_dir[1])
    return {(new_pos, new_dir)}



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    layout = [list(l) for l in lines]

    energized = set()
    num_energized = len(energized)
    num_since_last_update = 0
    # The coordinate is (row, col), followed by direction. Use a tuple so it can
    # be hashed / deduped.
    rays = [((0, 0), "r")]

    while len(rays) != 0 and num_since_last_update < 50:
        new_rays = []
        for r in rays:
            energized.add(r[0])
            new_rays += go_to_next(layout, r)

        new_rays = {r for r in new_rays if is_valid_pos(layout, r[0])}
        rays = new_rays

        if len(energized) > num_energized:
            num_since_last_update = 0
            num_energized = len(energized)
        else:
            num_since_last_update += 1

    return len(energized)


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 46


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
