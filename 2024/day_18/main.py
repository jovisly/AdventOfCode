"""
Reflections: Nice chill break after a few tough days. For Part 2, started with just
incrementing the number for the search, but then also parallely tested lower and upper
bounds to restrict search space and quickly arrived at the answer.
"""
import utils
import heapq

filename = "input.txt"
max_val = 70
num_bytes = 1024
# filename = "input-test.txt"
# max_val = 6
# num_bytes = 12
lines = open(filename, encoding="utf-8").read().splitlines()
coords = [tuple(map(int, line.split(","))) for line in lines][:num_bytes]

dict_board = {
    (i, j): "#" if (i, j) in coords else "."
    for i in range(max_val + 1) for j in range(max_val + 1)
}
# print(dict_board)

s = (0, 0)
e = (max_val, max_val)
queue = [(0, s)]
visited = set()
visited.add(s)

while len(queue) > 0:
    n, pos = heapq.heappop(queue)
    if pos == e:
        print("Part 1:", n)
        break

    for neighbor in utils.get_neighbors(pos):
        if neighbor not in visited and neighbor in dict_board and dict_board[neighbor] == ".":
            heapq.heappush(queue, (n + 1, neighbor))
            visited.add(neighbor)



# utils.viz_board(dict_board)

def can_get_out(dict_board):
    s = (0, 0)
    e = (max_val, max_val)
    queue = [(0, s)]
    visited = set()
    visited.add(s)

    while len(queue) > 0:
        n, pos = heapq.heappop(queue)
        if pos == e:
            return True

        for neighbor in utils.get_neighbors(pos):
            if neighbor not in visited and neighbor in dict_board and dict_board[neighbor] == ".":
                heapq.heappush(queue, (n + 1, neighbor))
                visited.add(neighbor)
    return False

# Testing area for upper / lower bounds
# n = 2950
# coords = [tuple(map(int, line.split(","))) for line in lines][:n]
# dict_board = {
#     (i, j): "#" if (i, j) in coords else "."
#     for i in range(max_val + 1) for j in range(max_val + 1)
# }
# print(can_get_out(dict_board))
# exit()

# for n in range(num_bytes, len(lines)):
for n in range(2900, 2950):
    if n % 100 == 0:
        print("n:", n)
    coords = [tuple(map(int, line.split(","))) for line in lines][:n]
    dict_board = {
        (i, j): "#" if (i, j) in coords else "."
        for i in range(max_val + 1) for j in range(max_val + 1)
    }
    if not can_get_out(dict_board):
        print("CANT GET OUT:")
        print(n - 1, lines[n - 1])
        break


