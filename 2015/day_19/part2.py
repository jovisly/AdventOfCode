"""
Reflections: Oof, the most difficult question of 2015 (so far). First I tried
dijkstra. That was a nope despite a lot of experimentations with different cost
measures (string length, Levenshtein distance, etc).

Here I am reverting the search. Instead of from "e" to final string, we do it
the other way. We also introduce randomness. If string is not reducing in length,
just re-run it until it gets to "e".

I'm surprised this (randomness) worked as well. It seems like I can get stuck on
a bad path, so we just need to random out of it. It also seems like the problem
was designed to have a very specific path, so dijkstra here is not really doing
best path finding. We are just using heapq to prioritize collapsing the string.
"""
import heapq
import random
import re

def get_dict_re(replacements):
    dict_re = {}
    for line in replacements:
        i, o = line.split(" => ")
        # Note we are flipping in and out.
        dict_re[o] = i
    return dict_re


def get_replacements(orig, i, o):
    set_new = set()
    for match in re.finditer(i, orig):
        start, end = match.start(), match.end()
        new = orig[:start] + o + orig[end:]
        set_new.add(new)
    return set_new



def get_all_replacements(curr_str, dict_re):
    set_new_all = set()
    for i, o in dict_re.items():
        set_new = get_replacements(curr_str, i, o)
        set_new_all = set_new_all.union(set_new)

    return set_new_all



def solve(filename):
    lines = open(filename, encoding="utf-8").read().split("\n\n")
    replacements = lines[0].splitlines()
    target = lines[1].strip()

    # Seems like the outputs are unique, which opens up some ideas.
    outs = [r.split(" => ")[1] for r in replacements]
    assert len(outs) == len(set(outs))

    # Then we can construct a dictionary keyed on "out" as they are unique.
    dict_re = get_dict_re(replacements)
    assert len(dict_re) == len(outs)

    # Now let's say we start with the target, and the target is actually "e".
    start = target
    target = "e"
    queue = [(len(start), round(random.random(), 2), 0, start)]
    visited = {start}
    found = False
    min_length = len(start)

    while len(queue) > 0 and not found:
        _, _, curr_num_steps, curr_str = heapq.heappop(queue)
        new_num_steps = curr_num_steps + 1

        # Find all the ways we can replace curr_str.
        all_new_str = get_all_replacements(curr_str, dict_re)
        all_new_str = [s for s in all_new_str if s not in visited]

        for new_str in all_new_str:
            if len(new_str) < min_length:
                min_length = len(new_str)
                # If we get stuck, just run again.
                print("New min length:", min_length)
                print(new_str)

            if new_str == target:
                found = True
                print("Got target string at step:", new_num_steps)
            else:
                new_queue = (
                    # Prioritize on shorter string.
                    len(new_str),
                    # randomness for luck. This is placed before num steps so
                    # that randomness is used before num steps as priority.
                    round(random.random(), 2),
                    new_num_steps,
                    new_str
                )
                heapq.heappush(queue, new_queue)
                visited.add(new_str)



if __name__ == "__main__":
    filename = "input.txt"
    solve(filename)
