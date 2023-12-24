def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    trees = [[int(u) for u in list(t)] for t in lines]

    num_visible = 0
    for r in range(len(trees)):
        for c in range(len(trees[r])):
            if r == 0 or c == 0:
                num_visible += 1
            elif r == len(trees) - 1 or c == len(trees[r]) - 1:
                num_visible += 1
            else:
                # Not at the edge so compare with neighbors.
                # A tree is visible if it can be viewed from one of the four
                # directions. Can be viewed means it's taller than any of those.
                this_tree_height = trees[r][c]

                this_row = trees[r]
                other_trees_1 = this_row[:c]
                other_trees_2 = this_row[c+1:]

                this_col = [t[c] for t in trees]
                other_trees_3 = this_col[:r]
                other_trees_4 = this_col[r+1:]

                if this_tree_height > max(other_trees_1) or \
                   this_tree_height > max(other_trees_2) or \
                   this_tree_height > max(other_trees_3) or \
                   this_tree_height > max(other_trees_4):
                    num_visible += 1

    return num_visible


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 21


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
