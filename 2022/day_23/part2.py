"""
Time: A couple of minutes on the code since I didn't change much from part 1.
Running the code took a while though.

Reflections: My code is not efficient at all. 10 rounds takes a few seconds from
Part 1. My expectation though is that essentially the elves are moving away from
each other. So I'm hoping that means it doesn't take that many rounds to get to
a stable state where no elf can move.

Ok I came back to the computer after a few hours and it's completed. It was about
900 rounds, and given about 1 sec per round, it would've been 15 minutes. Very
slow indeed.
"""
import utils
from part1 import propose_move, resolve_proposals, update_elves

def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()

    # Get coordinates of the elves.
    dict_elves = utils.get_dict_board(lines)
    list_elves = [
        k for k, v in dict_elves.items() if v == "#"
    ]

    round_num = 0
    while True:
        if round_num % 10 == 0:
            print("round num", round_num)
        proposals = {pos: propose_move(pos, list_elves, round_num) for pos in list_elves}

        if all([v is None for v in proposals.values()]):
            break

        proposals = resolve_proposals(proposals)
        list_elves = update_elves(list_elves, proposals)
        round_num += 1

    return round_num + 1


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 20


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
