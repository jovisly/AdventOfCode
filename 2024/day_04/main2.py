import utils

filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

dict_board = utils.get_dict_board(lines)
size = len(lines)


def count_stars(dict_board):
    c = 0
    for i in range(size):
        for j in range(size):
            # let (i, j) be the center of the star. There are five values we have to check.
            pos_cen = (i, j)
            pos_ur = (i + 1, j - 1)
            pos_ul = (i + 1, j + 1)
            pos_dr = (i - 1, j - 1)
            pos_dl = (i - 1, j + 1)
            if not all(p in dict_board for p in (pos_cen, pos_ur, pos_ul, pos_dr, pos_dl)):
                continue

            # There are four possible configurations we will accept. That's a lot to
            # manually check...
            if not dict_board[pos_cen] == "A":
                continue

            v_ur = dict_board[pos_ur]
            v_ul = dict_board[pos_ul]
            v_dr = dict_board[pos_dr]
            v_dl = dict_board[pos_dl]

            if v_ur == "M" and v_dl == "S" and v_ul == "M" and v_dr == "S":
                c += 1

            if v_ur == "S" and v_dl == "M" and v_ul == "M" and v_dr == "S":
                c += 1

            if v_ur == "M" and v_dl == "S" and v_ul == "S" and v_dr == "M":
                c += 1

            if v_ur == "S" and v_dl == "M" and v_ul == "S" and v_dr == "M":
                c += 1

    return c

print("Part 2:", count_stars(dict_board))
