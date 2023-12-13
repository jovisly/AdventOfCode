from part1 import is_mirror



def get_all_horizontal_mirrors(map):
    rows = map.split("\n")
    rows = [r for r in rows if r != ""]
    mirrors = []
    for i in range(len(rows)-1):
        row_num = i + 1
        # Check if this is a horizontal mirror.
        if is_mirror(row_num, rows):
            mirrors.append(100 * row_num)

    return mirrors



def get_all_vertical_mirrors(map):
    rows = map.split("\n")
    rows = [r for r in rows if r != ""]
    row_width = len(rows[0])
    cols = ["".join([r[i] for r in rows]) for i in range(row_width)]
    mirrors = []

    for i in range(len(cols)-1):
        col_num = i + 1
        if is_mirror(col_num, cols):
            mirrors.append(col_num)

    return mirrors



def find_mirror(map):
    # First we need to get the original mirror location.
    orig_vs = get_all_vertical_mirrors(map)
    orig_hs = get_all_horizontal_mirrors(map)

    for i, m in enumerate(map):
        if m in (".", "#"):
            new_map = map
            new_char = "#" if m == "." else "."
            new_map = new_map[:i] + new_char + new_map[i+1:]

            out = get_all_vertical_mirrors(new_map)
            for o in out:
                if o != 0 and o not in orig_vs:
                    return o

            out = get_all_horizontal_mirrors(new_map)
            for o in out:
                if o != 0 and o not in orig_hs:
                    return o


    print("WARNING: NO MIRROR FOUND")
    return 0


def solve(filename):
    lines = open(filename, encoding="utf-8").read()
    maps = lines.split("\n\n")

    total = 0
    for m in maps:
        total += find_mirror(m)

    return total


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 400


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)

