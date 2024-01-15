def is_mirror(row_num, rows):
    i_u = -1
    i_d = 0
    while row_num + i_u >= 0 and row_num + i_d < len(rows):
        row_up = rows[row_num + i_u]
        row_down = rows[row_num + i_d]
        if not all([ru==rd for ru, rd in zip(row_up, row_down)]):
            return False
        i_u -= 1
        i_d += 1

    return True


def get_horizontal_mirror(map):
    """If there's a horizontal mirror, return 100 * num rows above."""
    rows = map.split("\n")
    rows = [r for r in rows if r != ""]

    for i in range(len(rows)-1):
        row_num = i + 1
        # Check if this is a horizontal mirror.
        if is_mirror(row_num, rows):
            return 100 * row_num

    return 0


def get_vertical_mirror(map):
    """If there's a vertical mirror, return num columns to the left."""
    rows = map.split("\n")
    rows = [r for r in rows if r != ""]
    row_width = len(rows[0])
    cols = ["".join([r[i] for r in rows]) for i in range(row_width)]

    for i in range(len(cols)-1):
        col_num = i + 1
        if is_mirror(col_num, cols):
            return col_num

    return 0



def solve(filename):
    lines = open(filename, encoding="utf-8").read()
    maps = lines.split("\n\n")

    total = 0
    for m in maps:
        total += get_horizontal_mirror(m)
        total += get_vertical_mirror(m)

    return total


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 405


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
