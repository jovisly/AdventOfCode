from tqdm import tqdm
from part1 import ROCKS, initialize_rock_y, wind, fall

def solve(filename, num_rocks=1000000000000):
    lines = open(filename, encoding="utf-8").read().splitlines()
    dirs = list(lines[0])
    rock_pos = set()
    max_y_pos = -1
    ind_dir = 0

    for i in tqdm(range(num_rocks)):
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
    assert solve(filename) == 1514285714288



if __name__ == "__main__":
    mini_test()

    # filename = "input.txt"
    # total = solve(filename)

    # print(total)
