"""
As expected even just coding the algo up took awhile, especially with the encoding
and decoding of the state. Kudos to people who can somehow do this within a few
minutes!

For part 1, the minimal number of steps turned out to be smaller than the example,
which caused me some confusion -- had to re-read the question several times to
realize the example was just an example, not the minimal path. I didn't optimize
the search too much, just by number of steps, and that still worked within one
minute.

For part 2, the search became too slow. I tried to add a prioritization on a
score based on how close items are to the fourth floor, with number of steps still
being the highest priority. But that still was taking a long time. So, we just
prioritize on that score first, then add a random priority, then run the search
a few times to get the min. That works instantaneously which is pretty cool. This
is a trick we learned for https://adventofcode.com/2015/day/19.

And with that, 2016 AoC is now completed.
"""
import heapq
import random
from itertools import combinations

PART2 = True

if PART2:
    filename = "input-part2.txt"
else:
    filename = "input.txt"

lines = open(filename, encoding="utf-8").read().splitlines()



# We need a way to encode a state, so that we don't revisit the same state. A
# state will be encoded in the following way as a simple string:
# "1:E,hydrogen-m,lithium-m|2:hydrogen-g|3:lithium-g|4:"
# print(lines)

def process_line(line):
    comps = line.split(" ")
    items = []
    for ind, comp in enumerate(comps):
        if comp.endswith("-compatible"):
            name = comp.split("-")[0]
            items.append(name + "-m")
        if comp.startswith("generator"):
            name = comps[ind - 1]
            items.append(name + "-g")
    return ",".join(sorted(items))


def get_initial_state(lines):
    initial_state = ""
    for i, line in enumerate(lines):
        floor = i + 1
        initial_state += f"{floor}:"
        if floor == 1:
            initial_state += "E,"
        floor_items = process_line(line)
        initial_state += floor_items
        if floor != 4:
            initial_state += "|"

    return initial_state


def deserialize_state(str_state):
    comps = str_state.split("|")
    dict_state = {}
    e_pos = None
    for comp in comps:
        floor = int(comp.split(":")[0])
        items = comp.split(":")[1].split(",")
        if "E" in items:
            e_pos = floor
        items = [i for i in items if i != "E" and len(i) > 0]
        dict_state[floor] = items
    if e_pos is None:
        raise Exception(f"No elevator found in state: {str_state}")
    return dict_state, e_pos


def get_score(dict_state):
    score = 0
    for floor, items in dict_state.items():
        multiplier = 4 - floor
        score += multiplier * len(items)
    return score


def get_next_state(curr_state, next_floor, moved_items):
    dict_state, e_pos = deserialize_state(curr_state)
    # Remove the items from the current floor.
    floor_items =  dict_state[e_pos]
    dict_state[e_pos] = [
        item for item in floor_items if item not in moved_items
    ]
    dict_state[next_floor] += moved_items

    # Get a score for this new configuration. Best config is to have all the
    # items on the fourth floor. So 0 for each item on the 4th, and 1 for each
    # on the 3rd, 2 for each on 2nd, and 3 for each on 3rd.
    score = get_score(dict_state)

    # Then we need to serialize state.
    str_state = ""
    for floor in [1, 2, 3, 4]:
        str_state += f"{floor}:"
        if floor == next_floor:
            str_state += "E,"

        items = dict_state[floor]
        str_state += ",".join(sorted(items))
        if floor != 4:
            str_state += "|"
    return str_state, score



def if_items_compatible(items):
    """Check if the list of items are compatible."""
    lonely_ms = []
    lonely_gs = []
    for item in items:
        n, t = item.split("-")
        if t == "g" and n + "-m" not in items:
            lonely_gs.append(item)
        if t == "m" and n + "-g" not in items:
            lonely_ms.append(item)

    if len(lonely_ms) > 0 and len(lonely_gs) > 0:
        return False
    else:
        return True


assert if_items_compatible(["cat-m", "cat-g", "dog-m", "dog-g", "ant-m"]) == True
assert if_items_compatible(["cat-m", "cat-g", "dog-g", "ant-m"]) == False
assert if_items_compatible(["cat-m", "cat-g"]) == True
assert if_items_compatible(["cat-g", "dog-g", "ant-g"]) == True
assert if_items_compatible(["cat-m", "dog-m"]) == True
assert if_items_compatible(["cat-m", "dog-m", "dog-g"]) == True
assert if_items_compatible(["cat-m", "dog-m", "dog-g", "cow-g"]) == False



initial_state = get_initial_state(lines)
print("===== Initial State =====")
print(initial_state)

dict_state, e_pos = deserialize_state(initial_state)

print()
print("===== Initial State Deserialized =====")
print(dict_state, e_pos)

score = get_score(dict_state)

queue = [(score, round(random.random(), 2), 0, initial_state)]
visited = {initial_state}

print()
print("===== Performing Search =====")
min_score = score
while len(queue) > 0:
    score, _, curr_cost, curr_state = heapq.heappop(queue)
    if score < min_score:
        min_score = score
        print("... new min score:", score)
    # Check if curr_state satisifies end condition.
    dict_state, e_pos = deserialize_state(curr_state)
    if (
        len(dict_state[1]) == 0 and
        len(dict_state[2]) == 0 and
        len(dict_state[3]) == 0
    ):
        print("FOUND! Number of steps:", curr_cost)
        # print("full_path:", full_path)
        exit()

    # Get where the elevator is and deduce all possible next moves.
    next_e_pos = [e_pos - 1, e_pos + 1]
    next_e_pos = [pos for pos in next_e_pos if pos >= 1 and pos <= 4]
    # print("next_e_pos:", next_e_pos)
    items = dict_state[e_pos]
    # Get combinations of different things we can take.
    options = list(combinations(items, 2)) + list(combinations(items, 1))
    valid_options = []
    for pos in next_e_pos:
        for option in options:
            list_option = list(option)
            # First filter out if bringing xxx-m and yyy-g. We assume m'd get
            # fried.
            compatible = if_items_compatible(list_option)
            if not compatible:
                continue

            # Next check if we bring these items to the next floor, would any m
            # get fried.
            items_next_floor = dict_state[pos] + list_option
            compatible = if_items_compatible(items_next_floor)
            if not compatible:
                continue

            # Create the encoding for next state.
            next_state, score = get_next_state(
                curr_state=curr_state,
                next_floor=pos,
                moved_items=list_option
            )

            # print("=" * 10)
            # print("moved items:", list_option)
            # print("next state:", next_state)
            if next_state not in visited:
                heapq.heappush(queue, (
                    score,
                    round(random.random(), 2),
                    curr_cost + 1,
                    next_state,
                    # full_path + f" ({str(list_option)} to {str(pos)}) =>\n" + next_state
                ))
                visited.add(next_state)




