"""
Time: 1.5 hour of coding, but I worked on this part over two sessions, and had a
lot of thinking time in between.

Bug report: This is more about optimization report. Initially I had a very slow
implementation where every step I'm redoing the blizzard movement. Then I cached
it manually but it was still slow (because I'm calculating from scratch again).
So I cached it better, then it was still not finishing. Printing out the position,
I saw that I was dealing with a lot of dupes. Keeping track of "visited" fixed that
and got me an answer that was however off by 1.

Wait actually I didn't have off-by-1 error. I had "printing the wrong thing"
error. Now THIS is a bug report.
"""
import heapq
import utils


def symbol_to_dir(sym):
    if sym == "<":
        return "L"
    elif sym == ">":
        return "R"
    elif sym == "^":
        return "U"
    elif sym == "v":
        return "D"
    else:
        raise Exception("Invalid symbol: ", sym)


def get_blizzards(lines):
    blizzards = []
    for row_idx, row in enumerate(lines):
        for col_idx, sym in enumerate(row):
            if sym in "<>^v":
                blizzards.append(((row_idx, col_idx), symbol_to_dir(sym)))
    return blizzards


def move_blizzard(blizzard, num_rows, num_cols):
    """A blizzard is in the format of ((4, 6), 'R')."""
    pos = blizzard[0]
    dir = blizzard[1]

    min_row = 1
    min_col = 1
    max_row = num_rows - 2
    max_col = num_cols - 2

    new_pos = utils.move_to_dir(pos, dir)

    if new_pos[0] < min_row:
        new_pos = (max_row, new_pos[1])
    elif new_pos[0] > max_row:
        new_pos = (min_row, new_pos[1])
    elif new_pos[1] < min_col:
        new_pos = (new_pos[0], max_col)
    elif new_pos[1] > max_col:
        new_pos = (new_pos[0], min_col)
    return (new_pos, dir)


def get_blizzards_at_t(blizzards, t, num_rows, num_cols):
    """Returns the blizzards at time t."""
    new_blizzards = []
    for b in blizzards:
        new_b = tuple(b)
        for _ in range(t):
            new_b = move_blizzard(new_b, num_rows, num_cols)
        new_blizzards.append(new_b)
    return new_blizzards



def get_blizzards_next_t(prev_blizzards, num_rows, num_cols):
    new_blizzards = []
    for b in prev_blizzards:
        new_b = tuple(b)
        new_b = move_blizzard(new_b, num_rows, num_cols)
        new_blizzards.append(new_b)
    return new_blizzards



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    dict_board = utils.get_dict_board(lines)
    # Get the coordinates that are not rocks. These are allowed (as long as the
    # blizzard is not there). We will keep track of the blizzards with another
    # data structure.
    set_pos_allowed = set([k for k, v in dict_board.items() if v != "#" ])
    num_rows = len(lines)
    num_cols = len(lines[0])

    start = (0, 1)
    end = (num_rows - 1, num_cols - 2)
    blizzards = get_blizzards(lines)

    # Our very own caching.
    dict_blizzards = {}

    # Queue is (cost, (i, j))
    queue = [(0, start)]

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
        if cost in dict_blizzards:
            curr_blizzards = dict_blizzards[cost]
        elif cost - 1 in dict_blizzards:
            prev_blizzards = dict_blizzards[cost - 1]
            curr_blizzards = get_blizzards_next_t(prev_blizzards, num_rows, num_cols)
            dict_blizzards[cost] = curr_blizzards
        else:
            curr_blizzards = get_blizzards_at_t(blizzards, cost, num_rows, num_cols)
            dict_blizzards[cost] = curr_blizzards

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
            if next_pos not in set_pos_allowed:
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



def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 18


if __name__ == "__main__":
    # mini_test()

    # Reset the global dictionaries after test and reset cache.
    filename = "input.txt"
    total = solve(filename)

    print(total)
    # 323 is too high.
    # 321 is too low lol.
