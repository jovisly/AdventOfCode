"""
Time: 11:15 - 11:39 (p1), p2 11:41-

Reflections: ...

Bug report: had "new = orig[:start] + o + orig[end + 1:]"
"""
import heapq
import math
import re

from Levenshtein import distance

def get_replacements(orig, replacement):
    i, o = replacement.split(" => ")

    set_new = set()
    for match in re.finditer(i, orig):
        start, end = match.start(), match.end()
        new = orig[:start] + o + orig[end:]
        set_new.add(new)
    return set_new


# Not helpful.
# def get_dict_re(input_txt):
#     dict_re = {}
#     for line in input_txt:
#         els = line.split(" => ")
#         i = els[0]
#         o = els[1]
#         if i in dict_re:
#             dict_re[i].append(o)
#         else:
#             dict_re[i] = [o]
#     return dict_re


# Extracted out from part 1.
def get_all_replacements(curr_str, replacements):
    set_new_all = set()
    for replacement in replacements:
        set_new = get_replacements(curr_str, replacement)
        set_new_all = set_new_all.union(set_new)
    return set_new_all



def solve(filename):
    lines = open(filename, encoding="utf-8").read().split("\n\n")
    replacements = lines[0].splitlines()
    orig = lines[1].strip()

    set_new_all = set()
    for replacement in replacements:
        set_new = get_replacements(orig, replacement)
        set_new_all = set_new_all.union(set_new)

    print("Part 1:", len(set_new_all))

    # Part 2: We will do a dijkstra.
    # Queue is num replacements and curr string.
    # However, this makes us get stuck on short strings because we would
    # prioritize less number of replacements. So let's make cost be number of
    # replacements plus diff of length.
    target = orig
    q = (0 + distance(target, "e"), 0, "e")
    # q = (0, "e")
    queue = [q]
    visited = {"e"}
    found = False
    max_length = 1
    min_dist = None
    while len(queue) > 0 and found == False:
        _, num_re, curr_str = heapq.heappop(queue)
        new_num_re = num_re + 1

        all_new_str = get_all_replacements(curr_str, replacements)
        # We know replacements always increase string length, so we can restrict this.
        all_new_str = [
            s for s in all_new_str if len(s) <= len(target) and s not in visited
        ]
        # print(":all_new_str:", len(all_new_str))
        for new_str in all_new_str:
            dist = distance(target, new_str)
            if min_dist is None or dist < min_dist:
                min_dist = dist
                print("New min distance:", dist)
            if len(new_str) > max_length:
                max_length = len(new_str)
                print("New string length:", max_length)

            if new_str == target:
                found = True
                print("Got target string at step:", new_num_re)
                break
            else:
                new_queue = (
                    new_num_re + dist / 2.,
                    new_num_re,
                    new_str
                )
                # Add curr state to queue.
                heapq.heappush(queue, new_queue)
                visited.add(new_str)


    print("Part 2:", new_num_re)



if __name__ == "__main__":
    filename = "input.txt"
    solve(filename)
    # 198 is too low.


