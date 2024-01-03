"""Doing 1000_000_000_000 using the same method from part1 doesn't work.

For the actual input, there are 15488 directions. Given there are 5 rocks, maybe
there will be patterns that repeat after 5 * 15488 = 77440 directions. So we
run the simulation for 10 * 100_000 rocks and see if we can find a pattern. The
extra 10x is just to be safe since we can still do it within a minute.

Note, the run time on the test dataset is about the same for the actual dataset
since it's the number of rocks that matters.

Bug report:

* While tracking how much height is added by each rock, I mistakenly have it
  track with component of the rock (i.e., every position in rock), leading to
  the wrong result that took a long time to debug.
"""

from tqdm import tqdm
from part1 import ROCKS, initialize_rock_y, wind, fall

def solve(filename, num_rocks=1000000000000, num_rocks_pattern=600):
    lines = open(filename, encoding="utf-8").read().splitlines()
    dirs = list(lines[0])
    print("Number of dir:", len(dirs))
    rock_pos = set()
    max_y_pos = -1
    ind_dir = 0

    list_heigh_incr = []

    for i in tqdm(range(num_rocks_pattern)):
        # First initialize the rock y position.
        ind_rock = i % len(ROCKS)
        rock = [(pos[0], pos[1]) for pos in ROCKS[ind_rock]]
        y = max_y_pos + 3 + 1
        rock = initialize_rock_y(rock, y)

        can_fall = True
        # When the rock can fall, keep falling. The rock always start as can
        # fall since it's starting above the max y.
        while can_fall:
            # Fall.
            dir = dirs[ind_dir]
            ind_dir = (ind_dir + 1) % len(dirs)
            rock = wind(rock, dir, rock_pos)
            rock, can_fall = fall(rock, rock_pos)

        # After we are done falling, add rock to the set of rock positions and
        # update max y position.
        old_max_y_pos = max_y_pos
        for pos in rock:
            rock_pos.add(pos)
            max_y_pos = max(max_y_pos, pos[1])

        list_heigh_incr.append(max_y_pos - old_max_y_pos)

    # Now let's try to get the periodicity. We don't know what it is. So we
    # guess.
    max_p = len(dirs) * len(ROCKS)
    while True:
        # Take the last max_p elements.
        list_heigh_incr_p = list_heigh_incr[-max_p:]
        # Then take the previous max_p elements.
        list_heigh_incr_pp = list_heigh_incr[-2 * max_p:-max_p]
        if all([x == y for x, y in zip(list_heigh_incr_p, list_heigh_incr_pp)]):
            print("Periodicity:", max_p)
            break
        max_p -= 1

    # Now we have priodicity, so we basically calculate the total by using the
    # periodicity measure. Iterating over will be way too slow, so what we will
    # do is to add them up in blocks.
    num_extra = num_rocks - num_rocks_pattern + max_p
    num_pattern_blocks = num_extra // max_p
    num_remainder = num_extra % max_p

    sum_pattern_start = sum(list_heigh_incr[:-max_p])
    sum_pattern_block = sum(list_heigh_incr_p)
    sum_pattern_remainer = sum(list_heigh_incr_p[:num_remainder])

    return sum_pattern_start + num_pattern_blocks * sum_pattern_block + sum_pattern_remainer



def mini_test():
    filename = "input-test.txt"
    assert solve(filename, num_rocks=2022, num_rocks_pattern=500) == 3068
    assert solve(filename, num_rocks_pattern=500) == 1514285714288



if __name__ == "__main__":
    mini_test()

    # Periodicity turned out to be 49590.
    filename = "input.txt"
    total = solve(filename, num_rocks_pattern=100_000)

    print(total)
