
def get_pos_vel(line):
    pos, vel = line.split("@")
    pos = pos.split(",")
    pos = pos[:2]
    pos = [int(p.strip()) for p in pos]
    vel = vel.split(",")
    vel = vel[:2]
    vel = [int(v.strip()) for v in vel]
    return pos, vel



def get_equation(pos, vec):
    """Given a position and its vector, get the line equation.

    y = mx + b
    """
    x1, y1 = pos
    another_pos = (x1 + vec[0], y1 + vec[1])
    x2, y2 = another_pos
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    return m, b


def get_intersect(eq1, eq2):
    """Given eq1 = (m1, b1), eq2 = (m2, b2), get the intersection point."""
    m1, b1 = eq1
    m2, b2 = eq2

    # Handle when lines don't intersect.
    if m1 == m2 and b1 == b2:
        raise ValueError("Lines are the same.")

    if m1 == m2:
        return None, None

    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return x, y


def is_in_range(x, y, min, max):
    return min <= x <= max and min <= y <= max


def is_in_future(pos_now, pos_next, vec):
    dx = pos_next[0] - pos_now[0]
    vx = vec[0]
    # Check they have the same sign.
    if dx * vx < 0:
        return False
    else:
        return True


def solve(filename, min, max):
    lines = open(filename, encoding="utf-8").read().splitlines()
    num = 0
    for i in range(len(lines)):
        pos1, vel1 = get_pos_vel(lines[i])
        for j in range(i + 1, len(lines)):
            pos2, vel2 = get_pos_vel(lines[j])
            eq1 = get_equation(pos1, vel1)
            eq2 = get_equation(pos2, vel2)
            x, y = get_intersect(eq1, eq2)
            if x is not None and y is not None and is_in_range(x, y, min, max):
                if is_in_future(pos1, (x, y), vel1) and is_in_future(pos2, (x, y), vel2):
                    num += 1

    return num


def mini_test():
    filename = "input-test.txt"
    assert solve(filename, min=7, max=27) == 2


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename, min=200000000000000, max=400000000000000)

    print(total)
