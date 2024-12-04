"""
Bug report: At first did not realize we can go forward AND backward, so was undercounting.

Also I went with tedious code instead of elegant code. Hence splitting off part 1 and part 2.
"""
import utils

filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

dict_board = utils.get_dict_board(lines)
size = len(lines)


def count_horizontal(dict_board):
    c = 0
    for i in range(size):
        for j in range(size):
            pos = ((i, j), (i, j + 1), (i, j + 2), (i, j + 3))
            if all(p in dict_board for p in pos):
                if dict_board[pos[0]] == "X" and dict_board[pos[1]] == "M" and dict_board[pos[2]] == "A" and dict_board[pos[3]] == "S":
                    c += 1
                if dict_board[pos[0]] == "S" and dict_board[pos[1]] == "A" and dict_board[pos[2]] == "M" and dict_board[pos[3]] == "X":
                    c += 1
    return c


def count_vertical(dict_board):
    c = 0
    for i in range(size):
        for j in range(size):
            pos = ((i, j), (i + 1, j), (i + 2, j), (i + 3, j))
            if all(p in dict_board for p in pos):
                if dict_board[pos[0]] == "X" and dict_board[pos[1]] == "M" and dict_board[pos[2]] == "A" and dict_board[pos[3]] == "S":
                    c += 1
                if dict_board[pos[0]] == "S" and dict_board[pos[1]] == "A" and dict_board[pos[2]] == "M" and dict_board[pos[3]] == "X":
                    c += 1
    return c


def count_diagonal_1(dict_board):
    c = 0
    for i in range(size):
        for j in range(size):
            pos = ((i, j), (i + 1, j + 1), (i + 2, j + 2), (i + 3, j + 3))
            if all(p in dict_board for p in pos):
                if dict_board[pos[0]] == "X" and dict_board[pos[1]] == "M" and dict_board[pos[2]] == "A" and dict_board[pos[3]] == "S":
                    c += 1
                if dict_board[pos[0]] == "S" and dict_board[pos[1]] == "A" and dict_board[pos[2]] == "M" and dict_board[pos[3]] == "X":
                    c += 1
    return c


def count_diagonal_2(dict_board):
    c = 0
    for i in range(size):
        for j in range(size):
            pos = ((i, j), (i + 1, j - 1), (i + 2, j - 2), (i + 3, j - 3))
            if all(p in dict_board for p in pos):
                if dict_board[pos[0]] == "X" and dict_board[pos[1]] == "M" and dict_board[pos[2]] == "A" and dict_board[pos[3]] == "S":
                    c += 1
                if dict_board[pos[0]] == "S" and dict_board[pos[1]] == "A" and dict_board[pos[2]] == "M" and dict_board[pos[3]] == "X":
                    c += 1
    return c

horz = count_horizontal(dict_board)
vert = count_vertical(dict_board)
diag1 = count_diagonal_1(dict_board)
diag2 = count_diagonal_2(dict_board)

print("Part 1:", horz + vert + diag1 + diag2)

