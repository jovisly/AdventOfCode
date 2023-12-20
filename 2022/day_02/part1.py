def get_score(my, yours):
    score = 0
    if my == "X":
        score += 1
    if my == "Z":
        score += 3
    if my == "Y":
        score += 2

    if my == "X":
        if yours == "A":
            score += 3
        if yours == "B":
            score += 0
        if yours == "C":
            score += 6

    if my == "Y":
        if yours == "A":
            score += 6
        if yours == "B":
            score += 3
        if yours == "C":
            score += 0

    if my == "Z":
        if yours == "A":
            score += 0
        if yours == "B":
            score += 6
        if yours == "C":
            score += 3

    return score


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    plays = [l.split(" ") for l in lines]
    return sum([get_score(play[1], play[0]) for play in plays])


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 15


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
