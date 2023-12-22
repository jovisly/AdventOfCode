"""We can't do the brute force search like part 1 anymore."""
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



def count_dots(row_str, diamond_row_width):
    num_diamonds = (diamond_row_width + 1) / 2
    mid_i = int((len(row_str) - 1) / 2)

    if num_diamonds % 2 == 0:
        max_i = int(num_diamonds / 2)
        num_dots = 0
    else:
        max_i = int((num_diamonds - 1) / 2)
        num_dots = 0 if row_str[mid_i] == "#" else 1

    for i in range(max_i):
        j = i * 2 + 1 if num_diamonds % 2 == 0 else (i + 1) * 2
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
def get_num_dots(row_str, diamond_row_width):
    if diamond_row_width > len(row_str):
        # The row is filled.
        num = 1 * get_num_dots(row_str, int((len(row_str) - 1) / 2), 0)
        num += count_num_extra_dots(row_str)
        return num
    else:
        # The row is not filled.
        return count_dots(row_str, diamond_row_width)



def solve(filename, num_steps):
    layout = open(filename, encoding="utf-8").read().splitlines()
    diamond_size = num_steps * 2 + 1
    layout_size = len(layout)

    total = 0
    for diamond_row_num in range(diamond_size):
        (layout_row_num, diamond_row_width) = get_row_info(
            layout_size, num_steps, diamond_row_num
        )
        total += get_num_dots(layout[layout_row_num], diamond_row_width)

    return total


def tdd():
    assert get_row_info(5, 4, 0) == (3, 1)
    assert get_row_info(5, 4, 1) == (4, 3)
    assert get_row_info(5, 4, 7) == (0, 3)
    assert get_row_info(5, 1, 1) == (2, 3)

    assert count_dots(".##.#.####.", 7) == 0
    assert count_dots(".##..S####.", 7) == 1

    assert count_dots(".##.#.####.", 5) == 2
    assert count_dots(".##.#.####.", 9) == 2
    assert count_dots(".##..S####.", 9) == 2


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
    mini_test()

    filename = "input.txt"
    # total = solve(filename, num_steps=26501365)
