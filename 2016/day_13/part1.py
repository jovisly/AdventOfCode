import heapq

import utils

# For test data.
INPUT = 10
END = (7, 4)

INPUT = 1350
END = (31, 39)

dict_board = {}

for x in range(50):
    for y in range(50):
        v = x*x + 3*x + 2*x*y + y + y*y + INPUT
        b = str(bin(v))[2:]
        if list(b).count("1") % 2 == 0:
            dict_board[(x, y)] = "."
        else:
            dict_board[(x, y)] = "#"


start = (1, 1)
end = END
queue = [(0, start)]
visited = {start}

while len(queue) > 0:
    curr_cost, curr_pos = heapq.heappop(queue)

    if curr_pos == end:
        print("FOUND!", curr_cost)
        exit()

    ns = utils.get_neighbors(curr_pos)
    ns = [n for n in ns if n in dict_board and dict_board[n] != "#" and n not in visited]
    for n in ns:
        heapq.heappush(queue, (curr_cost + 1, n))
        visited.add(n)
