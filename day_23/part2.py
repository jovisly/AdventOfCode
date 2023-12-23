"""This is an exhaustive search that prioritizes on longer path length.

So we can simply try the path length that's printed out.

This takes even longer than Part 1 as expected, and the first answer is not the
correct one.
"""
import copy
from part1 import is_valid, DIRS

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
    path_found = False
    while len(queue) > 0 and not path_found:
        # This effectively prioritizes the longest path.
        q = queue.pop()
        last_pos = q[-1]

        for dir in DIRS:
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
    assert solve(filename) == 154


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
    # 5402 is still too low.
    # 5426 is still too low.
    # 5526 not the right answer.
    # 5702 also not right.
    # 5870 also not right.
    # 6070 also not right.
    # 6078 also not right.
    # 6230 also not right but maybe we are getting close because "Curiously, it's the right answer for someone else"...

    # 9394 is the upper bound (num cells not #)
