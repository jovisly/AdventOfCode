import time
from curses import wrapper
from part1 import get_instruction, take_one_step, get_avg


def move_tail(h_pos, t_pos):
    """A variation to part 1's move_tail() that breaks down steps."""
    # print("h_pos", h_pos, "t_pos", t_pos)
    if (h_pos[0] == t_pos[0] and abs(h_pos[1] - t_pos[1]) == 2):
        # Head and tail are on the same row or column, and there is one cell
        # between them.
        return [(t_pos[0], get_avg(h_pos[1], t_pos[1]))]
    elif (h_pos[1] == t_pos[1] and abs(h_pos[0] - t_pos[0]) == 2):
        return [(get_avg(h_pos[0], t_pos[0]), t_pos[1])]
    elif (abs(h_pos[0] - t_pos[0]) == 2 and abs(h_pos[1] - t_pos[1]) == 1):
        return [
            (t_pos[0] , h_pos[1]),
            (get_avg(h_pos[0], t_pos[0]) , h_pos[1])
        ]
    elif (abs(h_pos[0] - t_pos[0]) == 1 and abs(h_pos[1] - t_pos[1]) == 2):
        return [
            (h_pos[0], t_pos[1]),
            (h_pos[0], get_avg(h_pos[1], t_pos[1]))
        ]
    else:
        # Don't trigger movement if it doesn't need to move.
        return None



def viz(stdscr, positions, offset_x=10, offset_y=10):
    stdscr.clear()
    for i, pos in enumerate(positions):
        y, x = pos
        label = "H" if i == 0 else str(i)
        stdscr.addstr(
            y + offset_y,
            x + offset_x,
            label
        )
    stdscr.refresh()



def solve(filename, stdscr):
    lines = open(filename, encoding="utf-8").read().splitlines()
    instructions = [get_instruction(line) for line in lines]
    origin = (0, 0)

    positions = [origin] * 10
    visited = set()

    for dir, dist in instructions:
        # print("***** INSTRUCTION *****", dir, dist)
        for _ in range(dist):
            # queue = [(0, take_one_step(positions[0], dir))]
            dict_queue = {i: [] for i in range(len(positions))}
            dict_queue[0] = [take_one_step(positions[0], dir)]
            while sum([len(v) for v in dict_queue.values()]) > 0:
                # Pick the queue with the biggest index with none zero length.
                ind = max([k for k, v in dict_queue.items() if len(v) > 0])
                queue = dict_queue[ind]
                # Take the first element.
                pos = queue[0]
                dict_queue[ind] = queue[1:]

                if ind == len(positions) - 1:
                    visited.add(pos)

                # Update the position according to queue.
                positions[ind] = pos
                time.sleep(1)
                viz(stdscr, positions)
                next_ind = ind + 1
                if next_ind < len(positions):
                    h_pos = positions[ind]
                    t_pos = positions[next_ind]
                    list_new_pos = move_tail(h_pos, t_pos)
                    if list_new_pos is not None:
                        dict_queue[next_ind] = list_new_pos

    # print("len", len(visited))
    return len(visited)


def mini_test(stdscr):
    filename = "input-test.txt"
    assert solve(filename, stdscr) == 1

    # filename = "input-test2.txt"
    # assert solve(filename) == 36


def main(stdscr):
    filename = "input-test.txt"
    solve(filename, stdscr)
    # mini_test(stdscr)

    # filename = "input.txt"
    # total = solve(filename)

    # print(total)
    stdscr.getch()


wrapper(main)
