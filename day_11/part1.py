def expand(image):
    """Identify rows and columns that should expand and expand."""
    list_rows = []
    list_columns = []

    for i, row in enumerate(image):
        if all([r == "." for r in row]):
            list_rows.append(i)

    for j, col in enumerate(zip(*image)):
        if all([c == "." for c in col]):
            list_columns.append(j)

    # Perform the expansion. i + row and i + col to shift the index as expansion
    # happens.
    for i, row in enumerate(list_rows):
        image.insert(i + row, ["." for _ in range(len(image[0]))])
    for i, col in enumerate(list_columns):
        for row in image:
            row.insert(i + col, ".")
    return image


def get_list_galaxies(image):
    galaxies = []
    for y, row in enumerate(image):
        for x, col in enumerate(row):
            if col == "#":
                galaxies.append((x, y))
    return galaxies


def get_sum_pairwise_dist(list_galaxies):
    sum_pairwise_dist = 0
    for i1, g1 in enumerate(list_galaxies):
        for i2, g2 in enumerate(list_galaxies):
            if i1 < i2:
                sum_pairwise_dist += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

    return sum_pairwise_dist


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    image = [list(line) for line in lines]
    image = expand(image)
    list_galaxies = get_list_galaxies(image)
    # for row in image:
    #     print("".join(row))

    return get_sum_pairwise_dist(list_galaxies)


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 374


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
