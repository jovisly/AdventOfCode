
def is_valid_pos(layout, pos):
    return (
        pos[0] >= 0 and pos[0] < len(layout)
        and pos[1] >= 0 and pos[1] < len(layout[0])
    )


def get_starting_point(layout):
    """Find the S."""
    for y in range(len(layout)):
        for x in range(len(layout[0])):
            if layout[y][x] == "S":
                return (y, x)


def take_one_step(layout, position):
    """Returns positions that can be reached from the current position."""
    set_new_pos = set()
    for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_pos = (position[0] + dir[0], position[1] + dir[1])
        if is_valid_pos(layout, new_pos) and layout[new_pos[0]][new_pos[1]] != "#":
            set_new_pos.add(new_pos)

    return set_new_pos



def solve(filename, num_steps):
    lines = open(filename, encoding="utf-8").read().splitlines()
    layout = [list(l) for l in lines]
    start_position = get_starting_point(layout)

    curr_positions = {start_position}
    for _ in range(num_steps):
        next_positions = set()
        for pos in curr_positions:
            out = take_one_step(layout, pos)
            next_positions = next_positions.union(out)

        curr_positions = next_positions

    return len(curr_positions)


def mini_test():
    filename = "input-test.txt"
    assert solve(filename, num_steps=6) == 16


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename, num_steps=64)

    print(total)
