from z3 import Int, Solver, Or, sat
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

    p_jolt = parts[-1][1:-1]
    p_jolt = p_jolt.split(",")
    return "".join(arr_goal), [p[1:-1] for p in p_moves], tuple(int(p) for p in p_jolt)


def find_min_num(line):
    _, buttons, goal = process_line(line)

    if all(g == 0 for g in goal):
        return 0

    solver = Solver()

    # Integer variables for how many times to press each button
    button_vars = [Int(f"button_{i}") for i in range(len(buttons))]

    # Each button variable must be non-negative
    for var in button_vars:
        solver.add(var >= 0)

    # Sum of button values must equal the goal
    for pos_idx in range(len(goal)):
        effect = 0
        for button_idx, button in enumerate(buttons):
            arr_button = [int(b) for b in button.split(",")]
            if pos_idx in arr_button:
                effect += button_vars[button_idx]

        solver.add(effect == goal[pos_idx])

    # Find minimum.
    min_total = None
    while solver.check() == sat:
        model = solver.model()
        total = sum(model[var].as_long() for var in button_vars)
        if min_total is None or total < min_total:
            min_total = total

        # Add constraint to exclude this solution to find others.
        solver.add(Or([button_vars[i] != model[button_vars[i]].as_long()
                      for i in range(len(button_vars))]))

    return min_total if min_total is not None else 0


tot = 0
for line in tqdm(lines):
    if line.strip():
        tot += find_min_num(line)

print("Part 2:", tot)

