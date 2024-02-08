import utils

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

board = """\
1 2 3
4 5 6
7 8 9
""".splitlines()

board = [l.split(" ") for l in board]

dict_board = utils.get_dict_board(board)

pos = (1, 1)
code = ""
for line in lines:
    dirs = list(line)
    for dir in dirs:
        next_pos = utils.move_to_dir(pos, dir)
        if next_pos in dict_board:
            pos = next_pos

    code += dict_board[pos]


print(code)


board = """\
x x 1 x x
x 2 3 4 x
5 6 7 8 9
x A B C x
x x D x x
""".splitlines()

board = [l.split(" ") for l in board]

dict_board = utils.get_dict_board(board)

pos = (2, 0)
code = ""
for line in lines:
    dirs = list(line)
    for dir in dirs:
        next_pos = utils.move_to_dir(pos, dir)
        if next_pos in dict_board and dict_board[next_pos] != "x":
            pos = next_pos

    code += dict_board[pos]


print(code)
