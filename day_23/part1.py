"""This is an exhaustive search that prioritizes on (approx) longer path length.

So we can simply try the path length that's printed out. We got pretty lucky and
the first result is the correct one.
"""
import copy

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def is_valid(board, pos):
    return (
        0 <= pos[0] < len(board) and
        0 <= pos[1] < len(board[0]) and
        board[pos[0]][pos[1]] != "#"
    )


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    board = [list(l) for l in lines]
    num_rows = len(board)
    num_cols = len(board[0])
    start = (0, 1)
    end = (num_rows - 1, num_cols -2)

    # Each queue is a complete path up until that point. When the last step of a
    # queue is the end point, move it to the completed list.
    queue = [[start]]
    completed = set()
    while len(queue) > 0:
        q = queue.pop()
        last_pos = q[-1]

        symbol = board[last_pos[0]][last_pos[1]]
        if symbol == "<":
            valid_dirs = [(0, -1)]
        elif symbol == ">":
            valid_dirs = [(0, 1)]
        elif symbol == "^":
            valid_dirs = [(-1, 0)]
        elif symbol == "v":
            valid_dirs = [(1, 0)]
        else:
            valid_dirs = DIRS

        for dir in valid_dirs:
            q_copy = copy.deepcopy(q)
            next_pos = (last_pos[0] + dir[0], last_pos[1] + dir[1])
            if is_valid(board, next_pos) and next_pos not in q_copy:
                q_copy.append(next_pos)
                if next_pos == end:
                    completed.add(tuple(q_copy))
                    print("ADDED A COMPLETED PATH: ", len(q_copy) - 1)
                else:
                    queue.append(q_copy)

    return max([len(c) - 1 for c in completed])


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 94


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
