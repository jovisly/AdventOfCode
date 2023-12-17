import heapq


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



def get_min_cost_dijkstra(board):
    # Each queue is (cost, i, j, curr_dir, num_steps_curr_dir)
    start = (0, 0)
    end = max(list(board))
    queue = [(0, *start, "r", 1), (0, *start, "d", 1)]
    visited = set()

    while len(queue) > 0:
        cost, i, j, curr_dir, num_steps_curr_dir = heapq.heappop(queue)

        if (i, j, curr_dir, num_steps_curr_dir) in visited:
            continue
        else:
            visited.add((i, j, curr_dir, num_steps_curr_dir))

        next_pos = (i + map_dir(curr_dir)[0], j + map_dir(curr_dir)[1])
        if next_pos not in board:
            continue

        new_cost = cost + board[next_pos]
        if next_pos == end:
            # Can't stop until it's moved at least this many steps.
            if num_steps_curr_dir >= 4:
                return new_cost

        for next_dir in ["r", "l", "u", "d"]:
            # No reverse.
            if map_dir(next_dir)[0] + map_dir(curr_dir)[0] == 0 and map_dir(next_dir)[1] + map_dir(curr_dir)[1] == 0:
                continue

            if next_dir != curr_dir and num_steps_curr_dir < 4:
                # Can't turn yet.
                continue

            if next_dir == curr_dir and num_steps_curr_dir >= 10:
                # Have to turn
                continue

            num_steps_next_dir = 1 if next_dir != curr_dir else num_steps_curr_dir + 1
            heapq.heappush(queue, (new_cost, *next_pos, next_dir, num_steps_next_dir))

    print("WARNING: No path found.")
    return 0


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    board = [list(l) for l in lines]
    # Turn it into a dictionary keyed on (i, j):
    board = {(i, j): int(val) for i, row in enumerate(board) for j, val in enumerate(row)}

    return get_min_cost_dijkstra(board)


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 94

    filename = "input-test2.txt"
    assert solve(filename) == 71


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
