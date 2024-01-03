"""
Notes on bugs:

* Getting the order of "fall" vs "wind" messed up.
* for wind(), I did not initially consider the wind blowing the rock into other
  rocks.
* ROCK_I was originally set up wrong, resulting in the wrong shape.

Debugging method: visualize the rocks with matplotlib.

coords = [...]
x_values = [coord[0] for coord in coords]
y_values = [coord[1] for coord in coords]

plt.scatter(x_values, y_values, marker='s', s=200)

plt.xlabel('X')
plt.ylabel('Y')
plt.show()
"""


# Each rock starts at two positions to the left. They are initialized at y = 0
# but we will need to move them depending on what other rocks are already there.
ROCK_HORIZ = [(2,0), (3,0), (4,0), (5,0)]
ROCK_CROSS = [(2,1), (3,1), (4,1), (3,0), (3,2)]
# This is reverse L instead of L.
ROCK_L = [(2,0), (3,0), (4,0), (4,1), (4,2)]
ROCK_I = [(2,0), (2,1), (2,2), (2,3)]
ROCK_SQUARE = [(2,0), (3,0), (2,1), (3,1)]

ROCKS = [ROCK_HORIZ, ROCK_CROSS, ROCK_L, ROCK_I, ROCK_SQUARE]


def initialize_rock_y(rock, y):
    return [(pos[0], pos[1] + y) for pos in rock]


def wind(rock, dir, rock_pos):
    new_rock = [(pos[0], pos[1]) for pos in rock]
    max_x = max([pos[0] for pos in new_rock])
    min_x = min([pos[0] for pos in new_rock])

    if dir == ">" and max_x < 6:
        new_rock = [(pos[0] + 1, pos[1]) for pos in new_rock]

    if dir == "<" and min_x > 0:
        new_rock = [(pos[0] - 1, pos[1]) for pos in new_rock]

    # Wind can't blow rock into another rock.
    for pos in new_rock:
        if pos in rock_pos:
            return rock

    return new_rock



def fall(rock, rock_pos):
    new_rock = [(pos[0], pos[1]) for pos in rock]
    new_rock = [(pos[0], pos[1] - 1) for pos in new_rock]

    # If cannot fall, return original rock.
    for pos in new_rock:
        if pos in rock_pos:
            return rock, False
        if pos[1] < 0:
            return rock, False

    return new_rock, True



def solve(filename, num_rocks):
    lines = open(filename, encoding="utf-8").read().splitlines()
    dirs = list(lines[0])
    rock_pos = set()
    max_y_pos = -1
    ind_dir = 0

    for i in range(num_rocks):
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
        for pos in rock:
            rock_pos.add(pos)
            max_y_pos = max(max_y_pos, pos[1])

    return max_y_pos + 1


def mini_test():
    filename = "input-test.txt"
    assert solve(filename, num_rocks=1) == 1
    assert solve(filename, num_rocks=2) == 4
    assert solve(filename, num_rocks=3) == 6
    assert solve(filename, num_rocks=4) == 7
    assert solve(filename, num_rocks=10) == 17
    assert solve(filename, num_rocks=2022) == 3068


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename, num_rocks=2022)

    print(total)
