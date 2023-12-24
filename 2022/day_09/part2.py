import os
import time

from part1 import get_instruction, take_one_step, get_avg


def move_tail(h_pos, t_pos):
    """A variation to part 1's move_tail() that adheres better the instruction:

    "if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up."
    """
    if (h_pos[0] == t_pos[0] and abs(h_pos[1] - t_pos[1]) == 2):
        # Head and tail are on the same row or column, and there is one cell
        # between them.
        return (t_pos[0], get_avg(h_pos[1], t_pos[1]))
    elif (h_pos[1] == t_pos[1] and abs(h_pos[0] - t_pos[0]) == 2):
        return (get_avg(h_pos[0], t_pos[0]), t_pos[1])
    elif h_pos[0] != t_pos[0] and h_pos[1] != t_pos[1] and (
        abs(h_pos[0] - t_pos[0]) > 1 or abs(h_pos[1] - t_pos[1]) > 1
    ):
        d0 = 1 if h_pos[0] > t_pos[0] else -1
        d1 = 1 if h_pos[1] > t_pos[1] else -1
        # Move diagonally in the direction of the head
        return (t_pos[0] + d0, t_pos[1] + d1)
    else:
        # Don't trigger movement if it doesn't need to move.
        return t_pos



def viz(positions, dir, dist, y_min=-20, y_max=5, x_min=-11, x_max=25):
    time.sleep(0.1)
    os.system('clear')
    print("\n")
    print(f" == {dir} {dist} ==")
    print()

    # Have a reversed version of positions.
    reversed_positions = positions[::-1]
    dict_positions = {
        pos: "H" if i == len(reversed_positions) - 1 else str(len(reversed_positions) - i - 1)
        for i, pos in enumerate(reversed_positions)
    }
    for y in range(y_min, y_max + 1):
        row = []
        for x in range(x_min, x_max + 1):
            if (y, x) in dict_positions:
                # Find the index of the position.
                row.append(dict_positions[(y, x)])
            else:
                row.append(".")
        print(" ", "".join(row))
    print()




def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    instructions = [get_instruction(line) for line in lines]
    origin = (0, 0)

    positions = [origin] * 10
    visited = set()

    for dir, dist in instructions:
        for _ in range(dist):
            for i in range(len(positions)):
                if i == 0:
                    # Move head
                    positions[i] = take_one_step(positions[i], dir)
                else:
                    # Move tail
                    positions[i] = move_tail(positions[i - 1], positions[i])
            # viz(positions, dir, dist)
            visited.add(positions[-1])

    # print("len", len(visited))
    return len(visited)


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 1

    filename = "input-test2.txt"
    assert solve(filename) == 36


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
