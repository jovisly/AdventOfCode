"""
Time: Solid couple of hours, including time to make the cube from paper. In
addition, after reading the problem description, I put off working on it for a
few weeks.

Reflection: I really didn't enjoy this problem (hence putting it off for so long).
It feels quite a chore to (a) map out the faces of the cube, and (b) handle the
boundary conditions. Maybe there's a way to generalize better. Also, after
starting to work on it, I realized the faces configuration for test data is totally
different than for the actual data, which is annoying and I ended up completely
not handling test data.
"""
from part1 import get_instructions, map_dir, turn

FACE_SIZE = 50

def get_next_pos_teleported(curr_face, curr_pos, dir):
    """Determine which face to teleport to. Hardcoded.

    There should be 6 * 4 = 24 cases.
    """
    r, c = curr_pos
    last = FACE_SIZE - 1
    if curr_face == 1 and dir == "U":
        return (6, (c, 0)), "R"
    elif curr_face == 1 and dir == "D":
        return (3, (0, c)), "D"
    elif curr_face == 1 and dir == "L":
        return (4, (last - r, 0)), "R"
    elif curr_face == 1 and dir == "R":
        return (2, (r, 0)), "R"
    elif curr_face == 2 and dir == "U":
        return (6, (last, c)), "U"
    elif curr_face == 2 and dir == "D":
        return (3, (c, last)), "L"
    elif curr_face == 2 and dir == "L":
        return (1, (r, last)), "L"
    elif curr_face == 2 and dir == "R":
        return (5, (last - r, last)), "L"
    elif curr_face == 3 and dir == "U":
        return (1, (last, c)), "U"
    elif curr_face == 3 and dir == "D":
        return (5, (0, c)), "D"
    elif curr_face == 3 and dir == "L":
        return (4, (0, r)), "D"
    elif curr_face == 3 and dir == "R":
        return (2, (last, r)), "U"
    elif curr_face == 4 and dir == "U":
        return (3, (c, 0)), "R"
    elif curr_face == 4 and dir == "D":
        return (6, (0, c)), "D"
    elif curr_face == 4 and dir == "L":
        return (1, (last - r, 0)), "R"
    elif curr_face == 4 and dir == "R":
        return (5, (r, 0)), "R"
    elif curr_face == 5 and dir == "U":
        return (3, (last, c)), "U"
    elif curr_face == 5 and dir == "D":
        return (6, (c, last)), "L"
    elif curr_face == 5 and dir == "L":
        return (4, (r, last)), "L"
    elif curr_face == 5 and dir == "R":
        return (2, (last - r, last)), "L"
    elif curr_face == 6 and dir == "U":
        return (4, (last, c)), "U"
    elif curr_face == 6 and dir == "D":
        return (2, (0, c)), "D"
    elif curr_face == 6 and dir == "L":
        return (1, (0, r)), "D"
    elif curr_face == 6 and dir == "R":
        return (5, (last, r)), "U"
    else:
        raise ValueError(f"Unhandled face and direction: {curr_face}, {dir}")


def take_one_step(curr_pos, dir, dict_faces):
    face, pos = curr_pos
    dir_r, dir_c = map_dir(dir)
    r, c = pos
    next_pos = (r + dir_r, c + dir_c)

    if next_pos in dict_faces[face]:
        dict_board = dict_faces[face]
        if dict_board[next_pos] == "#":
            # We can't run into a wall, so just return what we had before.
            return curr_pos, dir
        else:
            # We can keep moving on this same face.
            return (face, next_pos), dir
    else:
        # Boundary condition. Hard coded.
        p, d = get_next_pos_teleported(face, pos, dir)
        f = p[0]
        if dict_faces[f][p[1]] == "#":
            return curr_pos, dir
        else:
            return p, d



def split_into_two_faces(face):
    f1 = []
    f2 = []
    for row in face:
        cleaned = row.strip()
        assert len(cleaned) == 2 * FACE_SIZE
        r1 = cleaned[:FACE_SIZE]
        r2 = cleaned[FACE_SIZE:]
        f1.append(r1)
        f2.append(r2)
    return f1, f2


def get_dict_board(board):
    return {(i, j): val for i, row in enumerate(board) for j, val in enumerate(row)}


def get_faces(board):
    """Assign faces to the board according to problem statement.

    The faces are laid out for the actual dataset and not compatible with test
    dataset, and have the following numbering:

    sec1    12
    sec2    3
    sec3   45
    s3c4   6
    """
    sec1 = board[:FACE_SIZE]
    f1, f2 = split_into_two_faces(sec1)

    sec2 = board[1*FACE_SIZE:2*FACE_SIZE]
    f3 = [row.strip() for row in sec2]

    sec3 = board[2*FACE_SIZE:3*FACE_SIZE]
    f4, f5 = split_into_two_faces(sec3)

    sec4 = board[3*FACE_SIZE:4*FACE_SIZE]
    f6 = [row.strip() for row in sec4]

    dict_faces = {
        1: get_dict_board(f1),
        2: get_dict_board(f2),
        3: get_dict_board(f3),
        4: get_dict_board(f4),
        5: get_dict_board(f5),
        6: get_dict_board(f6),
    }
    return dict_faces


def convert_pos(curr_pos):
    """Convert curr_pos = (f, pos) to the full coordinate.

       x12
       x3
       45
       6
    """
    f, pos = curr_pos
    r, c = pos
    if f == 1:
        return (r, c + FACE_SIZE)
    elif f == 2:
        return (r, c + 2 * FACE_SIZE)
    elif f == 3:
        return (r + FACE_SIZE, c + FACE_SIZE)
    elif f == 4:
        return (r + 2 * FACE_SIZE, c)
    elif f == 5:
        return (r + 2 * FACE_SIZE, c + FACE_SIZE)
    elif f == 6:
        return (r + 3 * FACE_SIZE, c)
    else:
        raise ValueError(f"Unknown face: {f}")



def solve(filename):
    lines = open(filename, encoding="utf-8").read().split("\n\n")
    board = lines[0]
    board = board.split("\n")

    num_rows = len(board)
    num_cols = max([len(row) for row in board])

    # Pad the board with ending spaces.
    board = [row + " " * (num_cols - len(row)) for row in board]
    dict_faces = get_faces(board)

    curr_pos = (1, (0, 0))

    line_instructions = lines[1]
    instructions = get_instructions(line_instructions)
    curr_dir = "R"

    for steps, turn_dir in instructions:
        for _ in range(steps):
            curr_pos, curr_dir = take_one_step(curr_pos, curr_dir, dict_faces)
            print("moved to ", curr_pos[0], convert_pos(curr_pos), curr_dir)

        if turn_dir != "":
            curr_dir = turn(curr_dir, turn_dir)


    dir_score = {"R": 0, "L": 2, "U": 3, "D": 1}
    pos = convert_pos(curr_pos)
    return 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + dir_score[curr_dir]


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 5031


if __name__ == "__main__":
    # mini_test will not work.
    # mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
