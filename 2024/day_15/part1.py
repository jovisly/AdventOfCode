"""
Time: ...

Reflections: ...

Bug report: ...
"""
import utils

filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().split("\n\n")
board = lines[0].splitlines()
moves = [m for m in list(lines[1]) if len(m.strip()) > 0]

dict_board = utils.get_dict_board(board)

def get_robot(dict_board):
    for pos, val in dict_board.items():
        if val == "@":
            return pos

def get_dir(move):
    if move == "^":
        dir = "U"
    if move == ">":
        dir = "R"
    if move == "v":
        dir = "D"
    if move == "<":
        dir = "L"
    return dir


def one_move(dict_board, robot_pos, move):
    dir = get_dir(move)
    next_pos = utils.move_to_dir(robot_pos, dir)
    if next_pos not in dict_board:
        return dict_board

    next_val = dict_board.get(next_pos, None)
    if next_val == "#":
        return dict_board
    if next_val == ".":
        dict_board[next_pos] = "@"
        dict_board[robot_pos] = "."
        return dict_board
    # Interesting scenario. If the next position is a box, we need to check if we
    # can move it to the next position. But we need to do this check for everything
    # along the way.
    if next_val == "O":
        queue_to_move = [next_pos]

        # Look for everything that needs to be moved.
        while True:
            # print("queue_to_move", queue_to_move)
            this_pos = queue_to_move[-1]
            next_pos = utils.move_to_dir(this_pos, dir)
            next_val = dict_board[next_pos]
            if next_val == "O":
                # Another box! Then we need to consider this box again.
                queue_to_move.append(next_pos)
            elif next_val == "#":
                # Ran into a wall!  Then we can't move.
                queue_to_move = []
                break
            else:
                break

        # Now we have to move all the boxes in reverse order.
        if len(queue_to_move) > 0:
            for pos in reversed(queue_to_move):
                next_pos = utils.move_to_dir(pos, dir)
                dict_board[next_pos] = "O"
                dict_board[pos] = "."
            # Robot should move to the first of the box.
            dict_board[queue_to_move[0]] = "@"
            dict_board[robot_pos] = "."

    return dict_board


def viz_board(dict_board):
    for i in range(len(board)):
        full_line = ""
        for j in range(len(board[0])):
            full_line += dict_board[(i, j)]
        print(full_line)


def get_coord(pos):
    return 100 * pos[0] +  pos[1]

viz_board(dict_board)
for move in moves:
    # print("\nMove:", move)
    robot_pos = get_robot(dict_board)
    dict_board = one_move(dict_board, robot_pos, move)
    # viz_board(dict_board)

tot = 0
for pos, v in dict_board.items():
    if v == "O":
        tot += get_coord(pos)



print("Part 1:", tot)

