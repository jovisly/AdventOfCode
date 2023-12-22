"""This got the right answer but very slow (10 min).

We will improve it in part2 by doing better set management.
"""
from tqdm import tqdm

def get_brick(line):
    brick = line.split("~")
    brick = [tuple(end.split(",")) for end in brick]
    brick = [(int(end[0]), int(end[1]), int(end[2])) for end in brick]

    # We are going to fill up the space between the two ends.
    min_x = min(brick[0][0], brick[1][0])
    max_x = max(brick[0][0], brick[1][0])
    min_y = min(brick[0][1], brick[1][1])
    max_y = max(brick[0][1], brick[1][1])
    min_z = min(brick[0][2], brick[1][2])
    max_z = max(brick[0][2], brick[1][2])
    filled = []
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            for z in range(min_z, max_z + 1):
                filled.append((x, y, z))

    return filled



def get_set_occupied(bricks):
    occupied = set()
    for brick in bricks:
        for end in brick:
            occupied.add(end)
    return occupied



def fall_to(set_occupied, brick):
    """Move the brick to the lowest possible location."""
    curr_min_z = min((end[2] for end in brick))
    blocked = False
    has_moved = False

    while blocked == False and curr_min_z > 1:
        new_min_z = curr_min_z - 1
        new_brick = []
        for end in brick:
            new_end = (end[0], end[1], end[2] - 1)
            if new_end in set_occupied:
                blocked = True
                break

            new_brick.append(new_end)

        # If not blocked, then lower the brick.
        if blocked == False:
            brick = new_brick
            curr_min_z = new_min_z
            has_moved = True

    return has_moved, brick



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

    # Check if bricks can disappear without affecting other bricks.
    num_cannot_disappear = 0
    for i in tqdm(range(len(bricks))):
        for j in range(len(bricks)):
            if i == j:
                continue

            # We need to exclude the removed brick, and the brick being compared.
            new_bricks = [
                brick for k, brick in enumerate(bricks) if k != i and k != j
            ]
            set_occupied = get_set_occupied(new_bricks)
            has_moved, _ = fall_to(set_occupied, bricks[j])
            if has_moved:
                num_cannot_disappear += 1
                break

    return len(bricks) - num_cannot_disappear


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 5


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
