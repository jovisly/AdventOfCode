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



def get_min_path_dijkstra(dict_board, start, end):
    path_cost = {n: float("inf") for n in list(dict_board)}
    path_cost[start] = dict_board[start]

    prev_node = {n: None for n in list(dict_board)}

    # Queue is (cost, (i, j))
    queue = [(0, start)]

    while len(queue) > 0:
        cost, curr_pos = heapq.heappop(queue)

        if cost > path_cost[curr_pos]:
            continue

        for dir in ["r", "l", "u", "d"]:
            next_pos = (
                curr_pos[0] + map_dir(dir)[0],
                curr_pos[1] + map_dir(dir)[1]
            )
            if next_pos not in dict_board:
                continue

            if dict_board[next_pos] > dict_board[curr_pos] + 1:
                continue

            new_cost = cost + 1
            if new_cost < path_cost[next_pos]:
                path_cost[next_pos] = new_cost
                prev_node[next_pos] = curr_pos
                heapq.heappush(queue, (new_cost, next_pos))

    return path_cost[end]



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    board = [list(l) for l in lines]
    start, end = fine_start_end(board)

    # Turn it into a dictionary keyed on (i, j):
    dict_board = {(i, j): map_letter_to_num(val) for i, row in enumerate(board) for j, val in enumerate(row)}
    return get_min_path_dijkstra(dict_board, start, end)


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 31


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
