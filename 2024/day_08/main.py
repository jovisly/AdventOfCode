"""
Bug report: "Because the topmost A-frequency antenna overlaps with a 0-frequency antinode"
This tripped me up. Part 2, what else but infinite loop because I keep using "i". Also,
the fact that every position is also an antinode required extra attention.
"""
import utils

filename = "input.txt"
# filename = "input-test.txt"
# filename = "input-test2.txt"

lines = open(filename, encoding="utf-8").read().splitlines()

board = utils.get_dict_board(lines)

unique_vals = set([v for v in board.values() if v != "."])

def find_atns(board, val):
    seen = set()
    # Given a unique value, find all potential antinode localtions.
    positions = [p for p, v in board.items() if v == val]
    # We will do it pairwise.
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            p1 = positions[i]
            p2 = positions[j]

            dx, dy = p2[0] - p1[0], p2[1] - p1[1]
            atn1 = (p1[0] - dx, p1[1] - dy)
            atn2 = (p2[0] + dx, p2[1] + dy)

            if atn1 in board:
                seen.add(atn1)
            if atn2 in board:
                seen.add(atn2)

    return seen

seen = set()
for val in unique_vals:
    seen.update(find_atns(board, val))


for i in range(len(lines)):
    full_line = ""
    for j in range(len(lines[0])):
        if (i, j) in seen:
            full_line += "#"
        else:
            full_line += board[(i, j)]
    print(full_line)


print("Part 1:", len(seen))



def find_many_atns(board, val):
    seen = set()
    positions = [p for p, v in board.items() if v == val]
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            p1 = positions[i]
            p2 = positions[j]
            # These positions are also antinodes.
            seen.add(p1)
            seen.add(p2)

            dx, dy = p2[0] - p1[0], p2[1] - p1[1]

            ii = 1
            while True:
                atn1 = (p1[0] - dx * ii, p1[1] - dy * ii)
                if atn1 not in board:
                    break
                else:
                    seen.add(atn1)
                ii += 1

            ii = 1
            while True:
                atn2 = (p2[0] + dx * ii, p2[1] + dy * ii)
                if atn2 not in board:
                    break
                else:
                    seen.add(atn2)
                ii += 1
    return seen


seen = set()
for val in unique_vals:
    seen.update(find_many_atns(board, val))


for i in range(len(lines)):
    full_line = ""
    for j in range(len(lines[0])):
        if (i, j) in seen:
            full_line += "#"
        else:
            full_line += board[(i, j)]
    print(full_line)


print("Part 2:", len(seen))
