from tqdm import tqdm
from part1 import find_start_end, get_min_path_dijkstra


def find_all_a(board):
    list_a = []
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == "a":
                list_a.append((i, j))
    return list_a



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    board = [list(l) for l in lines]
    start, end = find_start_end(board)
    # Add all other "a"'s as a start.
    list_a = find_all_a(board)
    list_a = [start] + list_a

    dict_board = {(i, j): val for i, row in enumerate(board) for j, val in enumerate(row)}

    min = len(board) * len(board[0])
    for a in tqdm(list_a):
        path_length = get_min_path_dijkstra(dict_board, a, end)
        if path_length < min:
            min = path_length

    return min


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 29


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
