"""
Reflections: Not much to it but I made a lot of bugs.
"""
import utils
from itertools import product


filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().split("\n\n")
# print(lines)

# Top filled is lock
# Bottom filled is key
# 5 pins total

def is_key_or_lock(block):
    if block[0] == "#" * 5:
        return "lock"
    elif block[-1] == "#" * 5:
        return "key"
    else:
        raise ValueError("Invalid block")


def get_pins_key(block):
    pins = []
    for j in range(5):
        n = 0
        for i in range(0, 6):
            if block[i][j] == "#":
                n += 1
        pins.append(n)
    return pins


def get_pins_lock(block):
    pins = []
    for j in range(5):
        n = 0
        for i in range(1, 6):
            if block[i][j] == "#":
                n += 1
        pins.append(n)
    return pins


keys = []
locks = []

for line in lines:
    block = line.split("\n")
    block_type = is_key_or_lock(block)
    print("block:", block)
    if block_type == "key":
        keys.append(get_pins_key(block))
        print("it's a key:", get_pins_key(block))
    elif block_type == "lock":
        locks.append(get_pins_lock(block))
        # print("it's a lock:", get_pins_lock(block))
# print("keys", keys)
# print("locks", locks)
print("num keys", len(keys))
print("num locks", len(locks))

tot = 0
for key, lock in product(keys, locks):
    sums = [k + l for k, l in zip(key, lock)]
    print("** key", key)
    print(" lock", lock)
    print(" sums", sums)
    if all(s <= 5 for s in sums):
        tot += 1
        # print("yes")

print("Part 1:", tot)

