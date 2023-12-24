def get_instruction(line):
    dir, dist = line.split(" ")
    return dir, int(dist)


def map_dir(dir):
    if dir == "R":
        return (0, 1)
    elif dir == "L":
        return (0, -1)
    elif dir == "U":
        return (-1, 0)
    elif dir == "D":
        return (1, 0)
    else:
        raise ValueError(f"Unknown direction: {dir}")


def take_one_step(pos, dir):
    mapped_dir = map_dir(dir)
    return (pos[0] + mapped_dir[0], pos[1] + mapped_dir[1])


def get_avg(a, b):
    return int((a + b) / 2)


def move_tail(h_pos, t_pos):
    """Check on the positional conditions and determine if to move tail.

    Return the new or unchanged tail position.
    """
    if (h_pos[0] == t_pos[0] and abs(h_pos[1] - t_pos[1]) == 2):
        # Head and tail are on the same row or column, and there is one cell
        # between them.
        return (t_pos[0], get_avg(h_pos[1], t_pos[1]))
    elif (h_pos[1] == t_pos[1] and abs(h_pos[0] - t_pos[0]) == 2):
        return (get_avg(h_pos[0], t_pos[0]), t_pos[1])
    elif (abs(h_pos[0] - t_pos[0]) == 2 and abs(h_pos[1] - t_pos[1]) == 1):
        return (get_avg(h_pos[0], t_pos[0]) , h_pos[1])
    elif (abs(h_pos[0] - t_pos[0]) == 1 and abs(h_pos[1] - t_pos[1]) == 2):
        return (h_pos[0], get_avg(h_pos[1], t_pos[1]))
    else:
        return t_pos


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    instructions = [get_instruction(line) for line in lines]
    origin = (0, 0)
    h_pos = origin
    t_pos = origin
    visited = set()

    for dir, dist in instructions:
        for _ in range(dist):
            h_pos = take_one_step(h_pos, dir)
            t_pos = move_tail(h_pos, t_pos)
            visited.add(t_pos)

    return len(visited)


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 13


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
