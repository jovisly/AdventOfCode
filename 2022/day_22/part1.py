"""
Time: A good hour and a half.

Reflections: Oof...

Bug report: Way too many bugs to report. I'm still struggling to figure out a
coordinate system that works for me, despite now having gone through several of
these "board"-like AoC problems. I keep mixing row/col/x/y/width/height and
having to do endless mental gymnastics.

I also mis-interpreted the problem statement on how the instruction at the end
should be followed. I thought we are getting a list of (num steps, direction)
pairs, but turns out we end the list with some extra steps moving in that direction.
This caused a very painful bug because it passed for test case but not for the
actual data.
"""
import re

def map_dir(dir):
    if dir == "R":
        return (0, 1)
    elif dir == "L":
        return (0, -1)
    elif dir == "U":
        return (-1, 0)
    elif dir == "D":
        return (1, 0)
    else:
        raise ValueError(f"Unknown direction: {dir}")


def turn(orig_dir, turn_dir):
    if turn_dir == "R":
        if orig_dir == "R":
            next_dir = "D"
        elif orig_dir == "D":
            next_dir = "L"
        elif orig_dir == "L":
            next_dir = "U"
        elif orig_dir == "U":
            next_dir = "R"
        else:
            raise ValueError(f"Unknown direction: {orig_dir}")
    elif turn_dir == "L":
        if orig_dir == "R":
            next_dir = "U"
        elif orig_dir == "D":
            next_dir = "R"
        elif orig_dir == "L":
            next_dir = "D"
        elif orig_dir == "U":
            next_dir = "L"
        else:
            raise ValueError(f"Unknown direction: {orig_dir}")
    else:
        raise ValueError(f"Unknown turn: {turn_dir}")
    return next_dir



def get_instructions(line_instructions):
    matches = re.findall(r'(\d+)([RL]?)', line_instructions)
    return [(int(num), letter) for num, letter in matches]



def take_one_step(curr_pos, dir, dict_board, dict_min_max):
    dir_r, dir_c = map_dir(dir)
    curr_r, curr_c = curr_pos
    next_r = curr_r + dir_r
    next_c = curr_c + dir_c

    # Boundary condition.
    if dir_c > 0 and next_c > dict_min_max["row"][curr_r]["max"]:
        next_c = dict_min_max["row"][curr_r]["min"]
    elif dir_c < 0 and next_c < dict_min_max["row"][curr_r]["min"]:
        next_c = dict_min_max["row"][curr_r]["max"]
    elif dir_r > 0 and next_r > dict_min_max["col"][curr_c]["max"]:
        next_r = dict_min_max["col"][curr_c]["min"]
    elif dir_r < 0 and next_r < dict_min_max["col"][curr_c]["min"]:
        next_r = dict_min_max["col"][curr_c]["max"]

    if dict_board[(next_r, next_c)] == "#":
        # We can't run into a wall.
        return curr_pos

    return (next_r, next_c)



def get_min_max(dict_board, num_cols, num_rows):
    # Get the min max position of each row and each column.
    dict_min_max = {"row": {}, "col": {}}
    for r in range(num_rows):
        valid_pos = [j for j in range(num_cols) if dict_board[(r, j)] != " "]
        dict_min_max["row"][r] = {
            "min": min(valid_pos), "max": max(valid_pos)
        }

    for c in range(num_cols):
        valid_pos = [i for i in range(num_rows) if dict_board[(i, c)] != " "]
        dict_min_max["col"][c] = {
            "min": min(valid_pos), "max": max(valid_pos)
        }
    return dict_min_max


def solve(filename):
    lines = open(filename, encoding="utf-8").read().split("\n\n")
    board = lines[0]
    board = board.split("\n")
    num_rows = len(board)
    num_cols = max([len(row) for row in board])

    # Pad the board with ending spaces.
    board = [row + " " * (num_cols - len(row)) for row in board]
    dict_board = {(i, j): val for i, row in enumerate(board) for j, val in enumerate(row)}
    # print("dict_board", dict_board)

    dict_min_max = get_min_max(dict_board, num_cols, num_rows)
    curr_pos = (
        0,
        min([ind for ind, b in enumerate(board[0]) if b == "."])
    )
    line_instructions = lines[1]
    instructions = get_instructions(line_instructions)
    curr_dir = "R"

    for steps, turn_dir in instructions:
        for _ in range(steps):
            curr_pos = take_one_step(curr_pos, curr_dir, dict_board, dict_min_max)
            # print("moved to ", curr_pos)
        if turn_dir != "":
            curr_dir = turn(curr_dir, turn_dir)


    dir_score = {"R": 0, "L": 2, "U": 3, "D": 1}
    return 1000 * (curr_pos[0] + 1) + 4 * (curr_pos[1] + 1) + dir_score[curr_dir]


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 6032


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
