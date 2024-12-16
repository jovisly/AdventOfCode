"""
Bug report: forgot about checking if position is wall.
"""
import heapq
import utils

filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

dict_board = utils.get_dict_board(lines)

start_pos = [p for p, v in dict_board.items() if v == "S"][0]
end_pos = [p for p, v in dict_board.items() if v == "E"][0]

# Iniital direction is Eastward.
dir = "R"
queue = [(0, start_pos, dir)]
visited = set((start_pos, dir))

while len(queue) > 0:
    points, pos, dir = heapq.heappop(queue)
    if pos == end_pos:
        print("Part 1:", points)
        break

    # Try to move forward.
    new_pos = utils.move_to_dir(pos, dir)
    if new_pos in dict_board and (new_pos, dir) not in visited and dict_board[new_pos] != "#":
        heapq.heappush(queue, (points + 1, new_pos, dir))
        visited.add((new_pos, dir))

    # We can also try turning left or right.
    right_dir = utils.turn(dir, "R")
    left_dir = utils.turn(dir, "L")
    if (pos, right_dir) not in visited:
        heapq.heappush(queue, (points + 1000, pos, right_dir))
        visited.add((pos, right_dir))
    if (pos, left_dir) not in visited:
        heapq.heappush(queue, (points + 1000, pos, left_dir))
        visited.add((pos, left_dir))
