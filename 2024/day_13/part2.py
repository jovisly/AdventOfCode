"""
Reflections: Omg Z3.
"""
import z3
from tqdm import tqdm
import heapq

import utils

filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().split("\n\n")

# print(lines)
nt_a = 3
nt_b = 1
extra = 10000000000000

def process_config(line):
    lines = line.splitlines()
    button_a = lines[0]
    button_b = lines[1]
    prize = lines[2]

    button_a_x, button_a_y = button_a.split("X+")[1].split(", Y+")
    button_b_x, button_b_y = button_b.split("X+")[1].split(", Y+")
    prize_x, prize_y = prize.split("X=")[1].split(", Y=")

    return int(button_a_x), int(button_a_y), int(button_b_x), int(button_b_y), int(prize_x) + extra, int(prize_y) + extra


def find_min_t(ax, ay, bx, by, px, py):
    z3_solver = z3.Solver()
    # Number of times we press the two buttons.
    nb_a, nb_b = z3.Int("nb_a"), z3.Int("nb_b")
    z3_solver.add(px == nb_a * ax + nb_b * bx)
    z3_solver.add(py == nb_a * ay + nb_b * by)

    min_n_t = None

    while z3_solver.check() == z3.sat:
        model = z3_solver.model()
        a_val = model[nb_a].as_long()
        b_val = model[nb_b].as_long()
        n_t = a_val * nt_a + b_val * nt_b

        # Update best solution if this is the first or better solution
        if min_n_t is None or n_t < min_n_t:
            min_n_t = n_t

        # Add constraint to exclude this solution and find others
        z3_solver.add(z3.Or(nb_a != a_val, nb_b != b_val))

    return min_n_t


tot = 0
for line in tqdm(lines):
    ax, ay, bx, by, px, py = process_config(line)
    out = find_min_t(ax, ay, bx, by, px, py)
    if out is not None:
        tot += out


print("Part 2:", tot)

