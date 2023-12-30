from functools import cache
from part1 import parse


NEIGHBORS = {}
FLOW_RATES = {}
START_POS = "AA"

def populate_dictionaries(lines):
    for line in lines:
        valve, rate, dest = parse(line)
        NEIGHBORS[valve] = dest
        FLOW_RATES[valve] = rate


@cache
def get_max_pressure(pos, time_left, node_opened, is_elephant=False):
    if time_left == 0:
        if is_elephant == False:
            # When there's no time left, we essentially try again with another
            # 26 minutes for the elephant.
            return get_max_pressure(START_POS, 26, node_opened, is_elephant=True)
        else:
            return 0

    # Max pressure is the max over all the results. The result can come from (a)
    # simply walk to a neighbor, which reduces time by 1 minute, or (b) open
    # this current position, which adds flow rate to all future scores.

    # (a) walk to a neighbor.
    score = max(
        [get_max_pressure(n, time_left - 1, node_opened, is_elephant) for n in NEIGHBORS[pos]]
    )

    # (b) open this current position. But only do it if it has some flow rate,
    # and if it hasn't been opened.
    if FLOW_RATES[pos] > 0 and pos not in node_opened:
        node_opened_copy = set(node_opened)
        node_opened_copy.add(pos)
        score = max(
            score,
            get_max_pressure(pos, time_left - 1, frozenset(node_opened_copy), is_elephant) + FLOW_RATES[pos] * (time_left - 1)
        )

    return score



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    populate_dictionaries(lines)
    max_pressure = get_max_pressure(START_POS, 26, frozenset(), is_elephant=False)
    return max_pressure



def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 1707


if __name__ == "__main__":
    mini_test()

    NEIGHBORS = {}
    FLOW_RATES = {}
    get_max_pressure.cache_clear()

    filename = "input.txt"
    total = solve(filename)

    print(total)
