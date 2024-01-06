"""
Time: 5 minutes.

Reflections: Ok I guess the plain I went through with Part 1 manipulating the
index values was worthwhile, since that approach doesn't incur any additional
time penalty for Part 2, when each number is a lot bigger. There is the 10X
penalty for the extra rounds of mixing, but that's not too bad.
"""
from tqdm import tqdm
from part1 import mix_numbers, get_dict_nums

PUZZLE_KEY = 811589153


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    nums = [int(line) for line in lines]
    nums = [n * PUZZLE_KEY for n in nums]
    assert nums.count(0) == 1

    dict_nums, key_zero = get_dict_nums(nums)
    # Mix it 10 times.
    for _ in tqdm(range(10)):
        dict_nums = mix_numbers(nums, dict_nums)

    ind_zero = dict_nums[key_zero]
    i1 = (ind_zero + 1000) % len(nums)
    i2 = (ind_zero + 2000) % len(nums)
    i3 = (ind_zero + 3000) % len(nums)

    v = [k[0] for k, v in dict_nums.items() if v in [i1, i2, i3] ]
    return sum(v)


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 1623178306


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
