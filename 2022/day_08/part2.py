def get_score_view(tree_height, other_heights):
    score = 0
    for h in other_heights:
        score += 1
        if h >= tree_height:
            return score

    return score


def get_score(trees, r, c):
    """Get the scoree of the tree at (r, c)."""
    this_row = trees[r]
    tree_height = this_row[c]
    other_trees_1 = this_row[:c]
    other_trees_1.reverse()
    a = get_score_view(tree_height, other_trees_1)

    other_trees_2 = this_row[c+1:]
    b = get_score_view(tree_height, other_trees_2)

    this_col = [t[c] for t in trees]
    other_trees_3 = this_col[:r]
    other_trees_3.reverse()
    c = get_score_view(tree_height, other_trees_3)

    other_trees_4 = this_col[r+1:]
    d = get_score_view(tree_height, other_trees_4)
    return a * b * c * d




def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    lines = open(filename, encoding="utf-8").read().splitlines()
    trees = [[int(u) for u in list(t)] for t in lines]

    max_score = 0
    for r in range(len(trees)):
        for c in range(len(trees[r])):
            score = get_score(trees, r, c)
            if score > max_score:
                max_score = score

    return max_score


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 8


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
