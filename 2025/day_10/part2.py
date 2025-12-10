# TOO SLOW!!
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

    p_jolt = parts[-1][1:-1]
    # print("p_jolt:", p_jolt)
    p_jolt = p_jolt.split(",")
    # print("p_jolt:", p_jolt)
    return "".join(arr_goal), [p[1:-1] for p in p_moves], tuple(int(p) for p in p_jolt)



def press_button(curr: tuple, button: str) -> tuple:
    new = list(curr)
    arr_button = [int(b) for b in button.split(",")]
    for b in arr_button:
        new[b] = new[b] + 1
    return tuple(new)


def find_min_num(line):
    # print("line", line)
    _, buttons, goal = process_line(line)
    # print("buttons:", buttons)
    # print("goal:", goal)

    curr = tuple([0] * len(goal))
    # print("curr:", curr)
    if curr == goal:
        return 0

    # Press each button once. Priority queue is num pressed and curr state.
    queue = [(1, press_button(curr, b)) for b in buttons]
    # print("queue:", queue)
    visited = {curr}
    for _, state in queue:
        visited.add(state)
    # print("queue:", queue)

    while len(queue) > 0:
        num_pressed, curr_state = heapq.heappop(queue)
        # print("curr_state:", curr_state)
        if curr_state == goal:
            # print("FOUND!", num_pressed)
            # print("Num pressed:", num_pressed)
            # exit()
            return num_pressed

        # if num_pressed > 3:
        #     return num_pressed
        for b in buttons:
            new_state = press_button(curr_state, b)
            if new_state not in visited:
                visited.add(new_state)
                heapq.heappush(queue, (num_pressed + 1, new_state))


# out = find_min_num(lines[2])
# print(out)

tot = 0
for line in tqdm(lines):
        tot += find_min_num(line)

print("Part 2:", tot)

# out = find_min_num(lines[0])
# print(out)

# _, buttons, jolts = process_line(lines[0])
# print(buttons)
# print(jolts)

# out = press_button("0000", "0,1")
# print(out)
