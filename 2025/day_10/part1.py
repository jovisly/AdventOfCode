import heapq
from tqdm import tqdm
import utils

filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().splitlines()


def process_line(line):
    parts = line.split(" ")
    p_goal = parts[0]
    p_moves = parts[1:-1]
    # Process goals.
    p_goal = p_goal[1:-1]
    arr_goal = ["0" if pos == "." else "1" for pos in p_goal]
    # print(arr_goal)

    # Process moves.
    return "".join(arr_goal), [p[1:-1] for p in p_moves]


def press_button(curr: str, button: str) -> str:
    new = list(curr)
    arr_button = [int(b) for b in button.split(",")]
    for b in arr_button:
        if new[b] == "0":
            new[b] = "1"
        else:
            new[b] = "0"
    return "".join(new)


def find_min_num(line):
    # print("line", line)
    goal, buttons = process_line(line)

    curr = "0" * len(goal)
    if curr == goal:
        return 0

    # Press each button once. Priority queue is num pressed and curr state.
    queue = [(1, press_button(curr, b)) for b in buttons]
    visited = {curr}  # Track visited states to avoid infinite loops
    for _, state in queue:
        visited.add(state)
    # print("queue:", queue)

    while len(queue) > 0:
        num_pressed, curr_state = heapq.heappop(queue)
        if curr_state == goal:
            # print("FOUND!", num_pressed)
            return num_pressed
        for b in buttons:
            new_state = press_button(curr_state, b)
            if new_state not in visited:
                visited.add(new_state)
                heapq.heappush(queue, (num_pressed + 1, new_state))


tot = 0
for line in tqdm(lines):
    if line.strip():  # Skip empty lines
        tot += find_min_num(line)

# print(queue)

# print("goal:", goal)
# print("buttons:", buttons)

# # n = press_button("0011", "2,0")
# # print(n)

print("Part 1:", tot)


