def get_score(my, yours):
    score = 0
    if my == "X":
        score += 0
    if my == "Z":
        score += 6
    if my == "Y":
        score += 3

    # Need to lose.
    if my == "X":
        if yours == "A":
            score += 3
        if yours == "B":
            score += 1
        if yours == "C":
            score += 2

    # Need to draw.
    if my == "Y":
        if yours == "A":
            score += 1
        if yours == "B":
            score += 2
        if yours == "C":
            score += 3

    # Need to win.
    if my == "Z":
        if yours == "A":
            score += 2
        if yours == "B":
            score += 3
        if yours == "C":
            score += 1

    return score


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    plays = [l.split(" ") for l in lines]
    return sum([get_score(play[1], play[0]) for play in plays])


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 12


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
