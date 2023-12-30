from functools import cache

# Use global dictionaries so they don't have to be passed into the recursive
# function, which will get cached.

# Keyed on the node, with value being an array of neighboring nodes.
NEIGHBORS = {}
# Keyed on the node, with value being its flow rate.
FLOW_RATES = {}


def parse(s):
    valve = s[6:8]
    rate = int(s.split("rate=")[1].split(";")[0])
    dest = s.split(" valves ")[1].split(",") if "valves" in s else s.split(" valve ")[1].split(",")
    dest = [d.strip() for d in dest]
    return valve, rate, dest


def populate_dictionaries(lines):
    for line in lines:
        valve, rate, dest = parse(line)
        NEIGHBORS[valve] = dest
        FLOW_RATES[valve] = rate


@cache
def get_max_pressure(pos, time_left, node_opened):
    if time_left == 0:
        return 0

    # Max pressure is the max over all the results. The result can come from (a)
    # simply walk to a neighbor, which reduces time by 1 minute, or (b) open
    # this current position, which adds flow rate to all future scores.

    # (a) walk to a neighbor.
    score = max(
        [get_max_pressure(n, time_left - 1, node_opened) for n in NEIGHBORS[pos]]
    )

    # (b) open this current position. But only do it if it has some flow rate,
    # and if it hasn't been opened.
    if FLOW_RATES[pos] > 0 and pos not in node_opened:
        node_opened_copy = set(node_opened)
        node_opened_copy.add(pos)
        score = max(
            score,
            get_max_pressure(pos, time_left - 1, frozenset(node_opened_copy)) + FLOW_RATES[pos] * (time_left - 1)
        )

    return score



def solve(filename, start):
    lines = open(filename, encoding="utf-8").read().splitlines()
    populate_dictionaries(lines)

    return get_max_pressure(start, 30, frozenset())


def mini_test():
    filename = "input-test.txt"
    assert solve(filename, start="AA") == 1651


if __name__ == "__main__":
    mini_test()

    # Reset the global dictionaries after test and reset cache.
    NEIGHBORS = {}
    FLOW_RATES = {}
    get_max_pressure.cache_clear()

    filename = "input.txt"
    # I missed the part of the question that says "we always start at AA" and
    # made "start" a variable.
    total = solve(filename, start="AA")

    print(total)
