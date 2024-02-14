from functools import cache

import utils

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()
import hashlib
import utils

SALT = "abc"
SALT = "jlmsuwbz"

def find_repeats(str, repeat=3):
    window = []
    for c in list(str):
        window.append(c)
        window = window[(-1 * repeat):]
        if len(window) == repeat:
            if all([w == window[0] for w in window]):
                return window[0]

    return None


@cache
def get_hash(orig_key, num_stretch=2017):
    k = orig_key
    for _ in range(num_stretch):
        hashed = hashlib.md5(k.encode("utf-8"))
        k = hashed.hexdigest()

    return k


keys = []
i = 0
while True:
    combo = SALT + str(i)
    hashed_str = get_hash(combo)
    hashed_str_orig = hashed_str
    triple = find_repeats(hashed_str, repeat=3)
    if triple is not None:
        # See if there's another repeat in the next 1000 index.
        for j in range(1, 1001):
            combo = SALT + str(i + j)
            hashed_str = get_hash(combo)
            fiveple = find_repeats(hashed_str, repeat=5)
            if fiveple is not None and fiveple == triple:
                keys.append(hashed_str_orig)
                print("adding key:", i, hashed_str_orig)
                break

    if len(keys) == 64:
        print("i:", i)
        break

    i += 1
