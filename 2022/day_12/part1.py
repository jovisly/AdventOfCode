import heapq

def map_letter_to_num(letter):
    if letter == "S":
        return map_letter_to_num("a")
    if letter == "E":
        return map_letter_to_num("z")
    return ord(letter) - ord("a") + 1


def fine_start_end(board):
    start = None
    end = None
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == "S":
                start = (i, j)
            elif val == "E":
                end = (i, j)
    return start, end


def map_dir(dir):
    if dir == "r":
        return (0, 1)
    elif dir == "l":
        return (0, -1)
    elif dir == "u":
        return (-1, 0)
    elif dir == "d":
        return (1, 0)
    else:
        raise ValueError(f"Unknown direction: {dir}")



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    board = [list(l) for l in lines]
    start, end = fine_start_end(board)

    # Turn it into a dictionary keyed on (i, j):
    dict_board = {(i, j): map_letter_to_num(val) for i, row in enumerate(board) for j, val in enumerate(row)}

    # Each queue is (cost, i, j, curr_dir)
    queue = [(0, *start, "r"), (0, *start, "d"), (0, *start, "l"), (0, *start, "u")]
    visited = set()

    while len(queue) > 0:
        cost, i, j, curr_dir = heapq.heappop(queue)

        if (i, j, curr_dir) in visited:
            continue
        else:
            visited.add((i, j, curr_dir))

        next_pos = (i + map_dir(curr_dir)[0], j + map_dir(curr_dir)[1])
        if next_pos not in dict_board:
            continue
        # We can only visit the next position if it's only one more than the current position.
        if dict_board[next_pos] > dict_board[(i, j)] + 1:
            continue

        new_cost = cost + dict_board[next_pos]
        print("*** next_pos:", next_pos, curr_dir)
        if next_pos == end:
            print("new_cost:", new_cost)
            return new_cost

        for next_dir in ["r", "l", "u", "d"]:
            heapq.heappush(queue, (new_cost, *next_pos, next_dir))

    print("WARNING: No path found.")
    return 0


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 31


if __name__ == "__main__":
    mini_test()

    # filename = "input.txt"
    # total = solve(filename)

    # print(total)
