def get_expanded_rows_and_cols(image):
    """Identify rows and columns that should expand."""
    list_rows = []
    list_columns = []

    for i, row in enumerate(image):
        if all([r == "." for r in row]):
            list_rows.append(i)

    for j, col in enumerate(zip(*image)):
        if all([c == "." for c in col]):
            list_columns.append(j)

    return list_rows, list_columns



def get_list_galaxies(image):
    galaxies = []
    for y, row in enumerate(image):
        for x, col in enumerate(row):
            if col == "#":
                galaxies.append((x, y))
    return galaxies



def get_sum_pairwise_dist(list_galaxies, list_rows, list_cols, expansion_size):
    sum_pairwise_dist = 0
    for i1, g1 in enumerate(list_galaxies):
        for i2, g2 in enumerate(list_galaxies):
            if i1 < i2:
                x1, y1 = g1
                x2, y2 = g2
                # Find the num. of rows between y1 and y2.
                num_rows_between = len([r for r in list_rows if y1 < r < y2 or y2 < r < y1])
                num_cols_between = len([c for c in list_cols if x1 < c < x2 or x2 < c < x1])

                dx = abs(x1 - x2) - num_cols_between + num_cols_between * expansion_size
                dy = abs(y1 - y2) - num_rows_between + num_rows_between * expansion_size
                sum_pairwise_dist += dx + dy

    return sum_pairwise_dist



def solve(filename, expansion_size):
    lines = open(filename, encoding="utf-8").read().splitlines()
    image = [list(line) for line in lines]
    list_rows, list_columns = get_expanded_rows_and_cols(image)
    list_galaxies = get_list_galaxies(image)
    return get_sum_pairwise_dist(list_galaxies, list_rows, list_columns, expansion_size)


def mini_test():
    filename = "input-test.txt"
    assert solve(filename, expansion_size=2) == 374
    assert solve(filename, expansion_size=10) == 1030
    assert solve(filename, expansion_size=100) == 8410



if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename, expansion_size=1000000)

    print(total)
