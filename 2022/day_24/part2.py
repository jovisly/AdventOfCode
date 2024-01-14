"""
Time: 25 minutes.

Bug report: I got the wrong answer initially because I did not reset the global
variables between test dataset and the actual dataset.
"""
import heapq
import utils

from part1 import get_blizzards, get_blizzards_next_t, get_blizzards_at_t

DICT_BLIZZARDS = {}
NUM_ROWS = 0
NUM_COLS = 0
SET_POS_ALLOWED = set()
BLIZZARDS = []

def find_min_cost(start, end, curr_cost):
    # Queue is (cost, (i, j))
    queue = [(curr_cost, start)]
    num_iters = 0
    visited = set()
    num_iters = 0

    while len(queue) > 0:
        cost, curr_pos = heapq.heappop(queue)

        if curr_pos == end:
            print("Found a path with cost: ", cost - 1)
            return cost - 1

        num_iters += 1

        if num_iters % 5000 == 1:
            print(f"Iterm num {num_iters}. Cost: ", cost, "Curr pos: ", curr_pos)

        # Manual caching.
        if cost in DICT_BLIZZARDS:
            curr_blizzards = DICT_BLIZZARDS[cost]
        elif cost - 1 in DICT_BLIZZARDS:
            prev_blizzards = DICT_BLIZZARDS[cost - 1]
            curr_blizzards = get_blizzards_next_t(prev_blizzards, NUM_ROWS, NUM_COLS)
            DICT_BLIZZARDS[cost] = curr_blizzards
        else:
            curr_blizzards = get_blizzards_at_t(BLIZZARDS, cost, NUM_ROWS, NUM_COLS)
            DICT_BLIZZARDS[cost] = curr_blizzards

        curr_blizzards_pos = [b[0] for b in curr_blizzards]

        # If this position is not occupied by a blizzard, then we can also wait.
        if curr_pos not in curr_blizzards_pos:
            new_cost = cost + 1
            if (new_cost, *curr_pos) not in visited:
                heapq.heappush(queue, (new_cost, curr_pos))
                visited.add((new_cost, *curr_pos))

        # Then we can make a move.
        for dir in utils.DIRS4:
            next_pos = utils.move_to_dir(curr_pos, dir)
            # Can't move to a rock position. Can't go out of the board.
            if next_pos not in SET_POS_ALLOWED:
                continue

            # Can't move to a position that has a blizzard.
            if next_pos in curr_blizzards_pos:
                continue

            new_cost = cost + 1
            if (new_cost, *next_pos) not in visited:
                heapq.heappush(queue, (new_cost, next_pos))
                visited.add((new_cost, *next_pos))

    print("WARNING: No path found.")
    return 0


def solve(filename):
    # Reset.
    global DICT_BLIZZARDS, NUM_ROWS, NUM_COLS, SET_POS_ALLOWED, BLIZZARDS
    DICT_BLIZZARDS = {}
    NUM_ROWS = 0
    NUM_COLS = 0
    SET_POS_ALLOWED = set()
    BLIZZARDS = []

    lines = open(filename, encoding="utf-8").read().splitlines()
    dict_board = utils.get_dict_board(lines)
    # Get the coordinates that are not rocks. These are allowed (as long as the
    # blizzard is not there). We will keep track of the blizzards with another
    # data structure.
    SET_POS_ALLOWED = set([k for k, v in dict_board.items() if v != "#" ])
    NUM_ROWS = len(lines)
    NUM_COLS = len(lines[0])

    start = (0, 1)
    end = (NUM_ROWS - 1, NUM_COLS - 2)
    BLIZZARDS = get_blizzards(lines)

    curr_cost = find_min_cost(start=start, end=end, curr_cost=0)
    print("Round 1 cost:", curr_cost)

    curr_cost = find_min_cost(start=end, end=start, curr_cost=curr_cost)
    print("Round 2 cost:", curr_cost)

    curr_cost = find_min_cost(start=start, end=end, curr_cost=curr_cost)
    print("Round 3 cost:", curr_cost)

    return curr_cost



def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 54


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)

