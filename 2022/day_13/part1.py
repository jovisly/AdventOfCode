import ast


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a > b:
            return False
        if a < b:
            return True

        # If they are equal, return None and continue checking.
        return None

    a = [a] if isinstance(a, int) else a
    b = [b] if isinstance(b, int) else b

    for ai, bi in zip(a, b):
        result = compare(ai, bi)
        if result is not None:
            return result

    # We have gone through the list. Now check who runs out first.
    if len(a) > len(b):
        return False

    if len(b) > len(a):
        return True

    # Tied :-/
    # This is the aspect that tripped me up a lot. Test data doesn't have tying.
    return None



def solve(filename):
    lines = open(filename, encoding="utf-8").read().split("\n\n")
    lines = [l.splitlines() for l in lines]
    lines = [[ast.literal_eval(a) for a in l] for l in lines]

    good_inds = []
    for ind, pair in enumerate(lines):
        result = compare(pair[0], pair[1])
        if result == True:
            good_inds.append(ind+1)

    return sum(good_inds)


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 13


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)



