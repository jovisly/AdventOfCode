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
up. BUT IT IS ANNOYING TO CALCULATE THIS. Also that still seems to be too much
iteration.
"""
import math
from tqdm import tqdm

from part1 import get_starting_point
from functools import cache


def get_row_info(layout_size, num_steps, diamond_row_num):
    """Translates the diamond row number to the actual row number."""
    diamond_size = num_steps * 2 + 1
    offset = int((layout_size - diamond_size) / 2)
    actual_row_num = (diamond_row_num + offset) % layout_size

    # Returns the row number between 0 and len(layout_size), and the width of
    # the row.
    mid = num_steps
    diff = mid - abs(mid - diamond_row_num)
    return actual_row_num, (diff * 2 + 1)



def count_even_dots(row_str, mod):
    max_i = int(mod / 2)
    mid_i = int((len(row_str) - 1) / 2)
    num_dots = 0
    for i in range(max_i):
        j = i * 2 + 1
        x = mid_i - j
        y = mid_i + j
        if row_str[x] != "#":
            num_dots += 1
        if row_str[y] != "#":
            num_dots += 1

    return num_dots



def count_odd_dots(row_str, mod):
    mid_i = int((len(row_str) - 1) / 2)
    num_dots = 0 if row_str[mid_i] == "#" else 1

    max_i = int((mod - 1) / 2)
    for i in range(max_i):
        j = (i + 1) * 2
        x = mid_i - j
        y = mid_i + j
        if row_str[x] != "#":
            num_dots += 1
        if row_str[y] != "#":
            num_dots += 1

    return num_dots



def count_num_extra_dots():
    # TODO.
    pass




@cache
def get_num_dots(row_str, mod, num_layout_filled):
    if num_layout_filled > 0:
        # If the row is filled, then we can first get the number of dots in the
        # row, then get the mod.
        num = num_layout_filled * get_num_dots(row_str, int((len(row_str) - 1) / 2), 0)
        num += count_num_extra_dots(row_str, mod)
        return num
    else:
        if mod % 2 == 0:
            return count_even_dots(row_str, mod)
        else:
            return count_even_dots(row_str, mod)



def solve(filename, num_steps):
    lines = open(filename, encoding="utf-8").read().splitlines()
    layout = [list(l) for l in lines]
    layout_size = len(layout)

    print(layout)
    return 0


def tdd():
    assert get_row_info(5, 4, 0) == (3, 1)
    assert get_row_info(5, 4, 1) == (4, 3)
    assert get_row_info(5, 4, 7) == (0, 3)
    assert get_row_info(5, 1, 1) == (2, 3)

    assert count_even_dots(".##.#.####.", 4) == 0
    assert count_even_dots(".##..S####.", 4) == 1

    assert count_odd_dots(".##.#.####.", 3) == 2
    assert count_odd_dots(".##.#.####.", 5) == 2
    assert count_odd_dots(".##..S####.", 5) == 2


def mini_test():
    filename = "input-test.txt"
    assert solve(filename, num_steps=6) == 16
    # assert solve(filename, num_steps=10) == 50
    # assert solve(filename, num_steps=50) == 1594
    # assert solve(filename, num_steps=100) == 6536
    # assert solve(filename, num_steps=500) == 167004
    # assert solve(filename, num_steps=1000) == 668697
    # assert solve(filename, num_steps=5000) == 16733044



if __name__ == "__main__":
    tdd()
    # mini_test()

    filename = "input.txt"
    # total = solve(filename, num_steps=26501365)
