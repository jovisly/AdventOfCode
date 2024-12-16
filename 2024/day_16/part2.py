"""
Time: ...

Reflections: ...

Bug report:
"""
import heapq
import utils

filename = "input.txt"
filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

dict_board = utils.get_dict_board(lines)

start_pos = [p for p, v in dict_board.items() if v == "S"][0]
end_pos = [p for p, v in dict_board.items() if v == "E"][0]

# Iniital direction is Eastward.
dir = "R"
queue = [(0, start_pos, dir)]
visited = set()
visited.add((start_pos, dir))
min_points = None

while len(queue) > 0:
    points, pos, dir = heapq.heappop(queue)
    if pos == end_pos:
        if min_points is None:
            min_points = points


    # Try to move forward.
    new_pos = utils.move_to_dir(pos, dir)
    if new_pos in dict_board and (new_pos, dir) not in visited and dict_board[new_pos] != "#":
        if min_points is None or points + 1 < min_points:
            heapq.heappush(queue, (points + 1, new_pos, dir))
            visited.add((new_pos, dir))

    # We can also try turning left or right.
    right_dir = utils.turn(dir, "R")
    left_dir = utils.turn(dir, "L")
    if (pos, right_dir) not in visited and (min_points is None or points + 1000 < min_points):
        heapq.heappush(queue, (points + 1000, pos, right_dir))
        visited.add((pos, right_dir))
    if (pos, left_dir) not in visited and (min_points is None or points + 1000 < min_points):
        heapq.heappush(queue, (points + 1000, pos, left_dir))
        visited.add((pos, left_dir))



print("min_points:", min_points)
print(visited)
print("." * 10)
pos = set([v[0] for v in visited])
print(pos)
print("Part 2:", len(pos))



def viz_board(dict_board, pos):
    max_x = max([p[0] for p in dict_board.keys()])
    max_y = max([p[1] for p in dict_board.keys()])
    for i in range(max_x + 1):
        full_line = ""
        for j in range(max_y + 1):
            if (i, j) in pos:
                full_line += "O"
            else:
                full_line += dict_board[(i, j)]
        print(full_line)


viz_board(dict_board, pos)
