
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

DIRS4 = ["R", "L", "U", "D"]
DIRS8 = ["S", "W", "N", "E", "NE", "NW", "SE", "SW"]

def map_dir_8(dir):
    if dir == "E":
        return (0, 1)
    elif dir == "W":
        return (0, -1)
    elif dir == "N":
        return (-1, 0)
    elif dir == "S":
        return (1, 0)
    elif dir == "NE":
        return (-1, 1)
    elif dir == "NW":
        return (-1, -1)
    elif dir == "SE":
        return (1, 1)
    elif dir == "SW":
        return (1, -1)
    else:
        raise ValueError(f"Unknown direction: {dir}")


def move_to_dir(pos, dir):
    mapped_dir = map_dir(dir)
    return (pos[0] + mapped_dir[0], pos[1] + mapped_dir[1])


def get_neighbors(pos, num_dirs=4):
    if num_dirs == 4:
        return [move_to_dir(pos, d) for d in DIRS4]
    if num_dirs == 8:
        return [move_to_dir(pos, d) for d in DIRS8]

    raise ValueError(f"Unknown number of directions: {num_dirs}")


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
