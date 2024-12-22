"""
Reflections: Much nicer than yesterday.
"""
from functools import cache
import utils

filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

@cache
def mix(sn, n):
    """This returns what secret number should become."""
    return sn ^ n

@cache
def prune(sn):
    return sn % 16777216

@cache
def evolve(sn):
    # Calculate the result of multiplying the secret number by 64.
    # Then, mix this result into the secret number.
    # Finally, prune the secret number.
    n = 64 * sn
    sn = mix(sn, n)
    sn = prune(sn)

    # Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer.
    # Then, mix this result into the secret number. Finally, prune the secret number.
    n = int(sn / 32)
    sn = mix(sn, n)
    sn = prune(sn)

    # Calculate the result of multiplying the secret number by 2048.
    # Then, mix this result into the secret number. Finally, prune the secret number.
    n = 2048 * sn
    sn = mix(sn, n)
    sn = prune(sn)

    return sn


def evolve_n(sn, n=2000):
    for _ in range(n):
        sn = evolve(sn)
    return sn


if __name__ == "__main__":
    tot = 0
    for n in lines:
        o = evolve_n(int(n))
        tot += o


    print("Part 1:", tot)

