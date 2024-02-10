"""
Time: ...

Reflections: ...

Bug report: ...
"""
import utils

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()



NC = 50
NR = 6

# Test data
# NC = 7
# NR = 3

dict_board = {}

for r in range(NR):
    for c in range(NC):
        dict_board[(r, c)] = " "



def viz_board(dict_board, line):
    print("")
    print("===== VIZ:", line)
    for r in range(NR):
        row = "".join([dict_board[(r, c)] for c in range(NC)])
        print(row)



viz_board(dict_board, "")
for line in lines:
    if line.startswith("rect"):
        dim = line.split(" ")[-1]
        # There was a bug here that took me forever to fix. i had dim.split("x") (without the equality).
        # this worked for almost everything until when a dim is more than one digit T_T
        dim = dim.split("x")
        dimc = int(dim[0])
        dimr = int(dim[-1])
        for r in range(dimr):
            for c in range(dimc):
                dict_board[(r, c)] = "#"

    if line.startswith("rotate"):
        dir = line.split(" ")[1]
        ind = int(line.split(" ")[2].split("=")[-1])
        amt = int(line.split(" ")[-1])

        if dir == "column":
            for _ in range(amt):
                prev = [dict_board[(r, ind)] for r in range(NR)]
                for r in range(NR):
                    if r > 0:
                        dict_board[(r, ind)] = prev[r - 1]
                    else:
                        dict_board[(r, ind)] = prev[-1]



        if dir == "row":
            for _ in range(amt):
                prev = [dict_board[(ind, c)] for c in range(NC)]
                for c in range(NC):
                    if c > 0:
                        dict_board[(ind, c)] = prev[c - 1]
                    else:
                        dict_board[(ind, c)] = prev[-1]


    viz_board(dict_board, line)


cnts = len([v for v in dict_board.values() if v == "#"])
print("cnts:", cnts)
# 69 is not right
