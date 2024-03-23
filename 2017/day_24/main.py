# Problem type:
# ~~~~~~~~~~~~ queue ~~~~~~~~~~~~
# Since we are looking for max, I did exhaustive searches which took about a
# minute for each part.
import heapq
import random

filename = "input.txt"
comps = open(filename, encoding="utf-8").read().splitlines()

# Make sure there's no dupes.
assert len(comps) == len(set(comps))

def get_strength(bridge):
    comps = bridge.split("-")
    strength = 0
    for comp in comps:
        cs = comp.split("/")
        strength += sum([int(c) for c in cs])
    return strength


def fine_queue(comps):
    valids = [c for c in comps if "0" in c.split("/")]
    queue = []
    for valid in valids:
        gates = valid.split("/")
        gates.remove("0")
        queue.append((valid, gates[0], valid))
    return queue

# Each queue is (curr_comp, curr_gate, full_seq). This is an exhaustive search
# so not prioritizing.
queue = fine_queue(comps)
visited = set([q[0] for q in queue])
max_strength = 0

while len(queue) > 0:
    curr_comp, curr_gate, curr_seq = queue.pop(0)
    # print("curr_comp, curr_gate, curr_seq", curr_comp, curr_gate, curr_seq)
    comps_copy = [c for c in comps if c not in curr_seq.split("-")]
    # Find the next available option.
    options = [c for c in comps_copy if curr_gate in c.split("/")]
    # print("options:", options)
    if len(options) == 0:
        # Done withe the bridge; get strength.
        # print("** Completed:", curr_seq)
        strength = get_strength(curr_seq)
        if strength > max_strength:
            max_strength = strength
            # print("  updating max strength:", max_strength)
    else:
        for option in options:
            next_seq = curr_seq + "-" + option
            if next_seq not in visited:
                gates = option.split("/")
                gates.remove(curr_gate)
                queue.append((
                    option,
                    gates[0],
                    next_seq
                ))
                visited.add(next_seq)

# This takes a minute.
print("Part 1:", max_strength)

# Part 2; reset. Slight modification to part 1.
queue = fine_queue(comps)
visited = set([q[0] for q in queue])
max_strength = 0
max_length = 0

while len(queue) > 0:
    curr_comp, curr_gate, curr_seq = queue.pop(0)
    # print("curr_comp, curr_gate, curr_seq", curr_comp, curr_gate, curr_seq)
    comps_copy = [c for c in comps if c not in curr_seq.split("-")]
    # Find the next available option.
    options = [c for c in comps_copy if curr_gate in c.split("/")]
    # print("options:", options)
    if len(options) == 0:
        # Done withe the bridge; get strength.
        # print("** Completed:", curr_seq)
        strength = get_strength(curr_seq)

        if len(curr_seq.split("-")) > max_length:
            max_length = len(curr_seq.split("-"))
            max_strength = strength
        elif len(curr_seq.split("-")) == max_length:
            if strength > max_strength:
                max_strength = strength
    else:
        for option in options:
            next_seq = curr_seq + "-" + option
            if next_seq not in visited:
                gates = option.split("/")
                gates.remove(curr_gate)
                queue.append((
                    option,
                    gates[0],
                    next_seq
                ))
                visited.add(next_seq)

print("Part 2:", max_strength)
