"""This got the right answer but very slow (10 min)."""
from tqdm import tqdm
from part1 import get_brick, get_set_occupied, fall_to


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    bricks = [get_brick(line) for line in lines]
    bricks = sorted(bricks, key=lambda ends: min(end[2] for end in ends))

    set_occupied = get_set_occupied(bricks)
    new_bricks = []
    for brick in bricks:
        has_moved, brick = fall_to(set_occupied, brick)
        new_bricks += [brick]
        # If a block has moved, we need to update the coordinate set.
        if has_moved == True:
            set_occupied = get_set_occupied(new_bricks)

    # Update bricks.
    bricks = new_bricks
    set_occupied = get_set_occupied(new_bricks)

    # Check how many bricks are moved due to other bricks being removed. This is
    # like the initial falling of bricks.
    num_moved = 0
    for i in tqdm(range(len(bricks))):
        new_bricks = []
        for j in range(len(bricks)):
            if i == j:
                continue

            set_occupied = get_set_occupied(new_bricks)
            brick = bricks[j]
            has_moved, brick = fall_to(set_occupied, brick)
            new_bricks.append(brick)
            # If a block has moved, we need to update the coordinate set.
            if has_moved == True:
                num_moved += 1

    return num_moved


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 7


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
