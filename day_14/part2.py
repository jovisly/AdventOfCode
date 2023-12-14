"""Rotating 1000000000 cycles takes too long. Just do a few to find pattern.

Then we plot the pattern:
https://colab.research.google.com/drive/1besHCEs296eDpO7D8JO6F46w-4wnnXyo#scrollTo=B7zQBDMp6fSf
"""


import numpy as np
from tqdm import tqdm

from part1 import tilt as tiltNorth
from part1 import score


def tiltSouth(lines):
    lines = np.flipud(lines).tolist()
    lines = tiltNorth(lines)
    lines = np.flipud(lines).tolist()
    return lines


def tiltEast(lines):
    lines = np.rot90(lines).tolist()
    lines = tiltNorth(lines)
    lines = np.rot90(lines, 3).tolist()
    return lines


def tiltWest(lines):
    lines = np.rot90(lines, 3).tolist()
    lines = tiltNorth(lines)
    lines = np.rot90(lines).tolist()
    return lines


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    lines = [list(l) for l in lines]

    sequences = []
    for _ in tqdm(range(1000)):
        lines = tiltNorth(lines)
        lines = tiltWest(lines)
        lines = tiltSouth(lines)
        lines = tiltEast(lines)
        s = score(lines)
        sequences.append(s)


    # We just use the sequence to identify pattern.
    print(sequences)
    return None



def get_total_from_pattern(pattern, n_to_remove, n_cycles):
    n = n_cycles - n_to_remove
    return pattern[n % len(pattern) - 1]



def mini_test():
    filename = "input-test.txt"
    solve(filename)

    pattern = [68, 69, 69, 65, 64, 65, 63]
    n_to_remove = 8
    n_cycles = 1000000000

    assert get_total_from_pattern(pattern, n_to_remove, n_cycles) == 64


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    solve(filename)

    pattern = [94245, 94255, 94263, 94278, 94295, 94312, 94313, 94315, 94309, 94302, 94283, 94269, 94258, 94253]
    n_to_remove = 102
    n_cycles = 1000000000
    result = get_total_from_pattern(pattern, n_to_remove, n_cycles)
    print(result)



"""Visualizing the pattern sample code:
import matplotlib.pyplot as plt

plt.plot(a[:30], '-o')
plt.ylabel('Sequence')


for i in range(len(a)):
    plt.text(i, a[i], str(a[i]), ha='right')

plt.show()
"""
