"""We can't do the brute force search like part 1 anymore.

So let's first pretend there are no rocks. Then each step simply expands the
area in a grid like manner. This gives us a mathematical way to represent all
the positions reachable in N steps.

Then, for each location, we can check if it is occupied by a rock, and remove it
from the set of reachable positions.

The rocks will adhere to infinite boundary conditions, so this can also be done
with math.

We will remap our grid system to have S be at the origin.

Problem: the number of positions reachable in N steps is actually (N+1)x(N+1).
For the actual problem, that's 26501365 * 26501365. We can't iterate through
this (but hey we have an upper bound!).

Is there going to be a pattern? We tried to find a pattern but not seeing
anything. There's a trend for sure and we can fit lines if we want but unclear
how to extrapolate.

Pattern detection also doesn't work for the reason that we'd need to have the
pattern repeat itself, but the pattern is 131x131, and we can't run that many
steps.

There is another way. We know the area is diamond shaped, covering on top of a
periodic grid. So we only need to calculate the number of rocks that's in a grid
not completely covered by the diamond. All the other grids can simply be summed
up. BUT IT IS ANNOYING TO CALCULATE THIS.
"""
import math
from tqdm import tqdm

from part1 import get_starting_point


def take_one_step(layout, position):
    """Returns positions that can be reached from the current position."""
    set_new_pos = set()
    for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_pos = (position[0] + dir[0], position[1] + dir[1])
        # Support infinite boundary condition.
        new_pos_mod = (new_pos[0] % len(layout), new_pos[1] % len(layout[0]))
        if layout[new_pos_mod[0]][new_pos_mod[1]] != "#":
            set_new_pos.add(new_pos)

    return set_new_pos



def count_num_rocks(layout):
    num_rocks = 0
    for y in range(len(layout)):
        for x in range(len(layout[0])):
            if layout[y][x] == "#":
                num_rocks += 1

    proportion = num_rocks / (len(layout) * len(layout))
    return num_rocks, 1 - proportion



def solve(filename, num_steps):
    lines = open(filename, encoding="utf-8").read().splitlines()
    layout = [list(l) for l in lines]
    num_rocks, proportion = count_num_rocks(layout)
    print("rock proportion", proportion)
    start_position = get_starting_point(layout)

    curr_positions = {start_position}
    list_num_positions = []
    for i in range(num_steps):
        next_positions = set()
        for pos in curr_positions:
            out = take_one_step(layout, pos)
            next_positions = next_positions.union(out)

        curr_positions = next_positions

        # list_num_positions.append()
        list_num_positions.append(len(curr_positions) / ((i + 2) * (i + 2)))

    print(list_num_positions)
    return len(curr_positions)


def mini_test():
    filename = "input-test.txt"
    # assert solve(filename, num_steps=6) == 16
    # assert solve(filename, num_steps=10) == 50
    # assert solve(filename, num_steps=50) == 1594
    assert solve(filename, num_steps=100) == 6536
    # assert solve(filename, num_steps=500) == 167004
    # assert solve(filename, num_steps=1000) == 668697
    # assert solve(filename, num_steps=5000) == 16733044



if __name__ == "__main__":
    # mini_test()

    filename = "input.txt"
    # total = solve(filename, num_steps=26501365)

    lines = open(filename, encoding="utf-8").read().splitlines()
    layout = [list(l) for l in lines]
    num_rocks, proportion = count_num_rocks(layout)

    print("rock proportion", proportion)
    num_steps = 26501365

    area = (num_steps + 1) * (num_steps + 1)
    print(area * proportion)
    # 603200853774507 is too high


    # print(total)

    # That's a nope.
    # for i in tqdm(range(26501365)):
    #     for j in tqdm(range(26501365)):
    #         pass
