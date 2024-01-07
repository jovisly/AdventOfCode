
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


def get_dict_board(board):
    dict_board = {
        (i, j): val for i, row in enumerate(board)
        for j, val in enumerate(row)
    }
    return dict_board
