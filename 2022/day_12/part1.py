import heapq
import os
import time

VIZ = False

def map_letter_to_num(letter):
    if letter == "S":
        return map_letter_to_num("a")
    if letter == "E":
        return map_letter_to_num("z")
    return ord(letter) - ord("a") + 1


def find_start_end(board):
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



def get_min_path_dijkstra(dict_board, start, end, viz=VIZ):
    path_cost = {n: float("inf") for n in list(dict_board)}
    path_cost[start] = 0

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

            # We can only visit a node if it's at most 1 greater than the current node.
            if map_letter_to_num(dict_board[next_pos]) > map_letter_to_num(dict_board[curr_pos]) + 1:
                continue

            new_cost = cost + 1
            if new_cost < path_cost[next_pos]:
                path_cost[next_pos] = new_cost
                prev_node[next_pos] = curr_pos
                heapq.heappush(queue, (new_cost, next_pos))


    if viz == True:
        full_path = []
        curr_pos = end
        while curr_pos != start:
            full_path.append(curr_pos)
            curr_pos = prev_node[curr_pos]

        full_path.append(start)
        full_path.reverse()
        draw_board(dict_board, full_path)

    return path_cost[end]



def draw_board(dict_board, full_path):
    min_pos, max_pos = (min(list(dict_board)), max(list(dict_board)))
    for ind, p in enumerate(full_path):
        # This causes a lot of blinking and is not great. We will just take a
        # screenshot of the final result. We will use an alternative method like
        # cursor next time.
        time.sleep(0.05)
        os.system('clear')
        print("\n\n")
        for i in range(min_pos[0], max_pos[0] + 1):
            row = []
            for j in range(min_pos[1], max_pos[1] + 1):
                if (i, j) == p:
                    # Head is yellow background.
                    row.append('\x1b[1;30;43m' + dict_board[(i, j)] + '\x1b[0m')
                elif (i, j) in full_path and full_path.index((i, j)) < ind:
                    # Rest is while background.
                    row.append('\x1b[1;30;47m' + dict_board[(i, j)] + '\x1b[0m')
                elif (i, j) in dict_board:
                    row.append(dict_board[(i, j)])

            print("  ", "".join(row))
    # Give us time for screenshot.
    time.sleep(60)



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    board = [list(l) for l in lines]
    start, end = find_start_end(board)

    # Turn it into a dictionary keyed on (i, j):
    dict_board = {(i, j): val for i, row in enumerate(board) for j, val in enumerate(row)}
    return get_min_path_dijkstra(dict_board, start, end)


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 31


if __name__ == "__main__":
    # mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
