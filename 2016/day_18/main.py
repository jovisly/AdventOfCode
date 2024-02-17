from tqdm import tqdm

# Part 1
NUM_ROWS = 40
# Part 2
NUM_ROWS = 400000

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()
row = lines[0]


def make_row(row):
    new_row = ""
    for i, _ in enumerate(list(row)):
        if i == 0:
            nbs = [".", row[0], row[1]]
        elif i == len(row) - 1:
            nbs = [row[-2], row[-1], "."]
        else:
            nbs = [row[i-1], row[i], row[i+1]]

        l, c, r = nbs
        nt = "."
        if l == "^" and c == "^" and r == ".":
            nt = "^"
        if l == "." and c == "^" and r == "^":
            nt = "^"
        if l == "^" and c == "." and r == ".":
            nt = "^"
        if l == "." and c == "." and r == "^":
            nt = "^"
        new_row += nt
    return new_row


tot = 0
for i in tqdm(range(NUM_ROWS)):
    if i == 0:
        tot += row.count(".")
    else:
        row = make_row(row)
        tot += row.count(".")

print("tot:", tot)
