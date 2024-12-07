"""
Bug report: For part 1, took forever to realize we are not doing typical math where
multiplication is done before addition (because I didn't read the instructions!).
This part of the instruction is even bolded -- facepalm.
"""
from tqdm import tqdm

import itertools
import utils

filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

def parse_line(line):
    left, right = line.split(":")
    goal = int(left)
    nums = list(map(int, right.split()))
    return goal, nums

# out = parse_line(lines[0])
# print(out)
def try_ops(goal, nums):
    ops = ['+', '*']

    for operations in itertools.product(ops, repeat=len(nums)-1):
        result = nums[0]

        # Evaluate left to right
        for i, op in enumerate(operations):
            if op == '+':
                result += nums[i+1]
            else:
                result *= nums[i+1]

        if result == goal:
            return goal

    return 0


total = 0
for line in tqdm(lines):
    goal, nums = parse_line(line)
    total += try_ops(goal, nums)

print("Part 1:", total)

def try_ops_with_cat(goal, nums):
    ops = ['+', '*', '||']

    for operations in itertools.product(ops, repeat=len(nums)-1):
        result = nums[0]

        for i, op in enumerate(operations):
            if op == '+':
                result += nums[i+1]
            elif op == '*':
                result *= nums[i+1]
            else:
                result = int(str(result) + str(nums[i+1]))

        if result == goal:
            return goal

    return 0


total = 0
for line in tqdm(lines):
    goal, nums = parse_line(line)
    total += try_ops_with_cat(goal, nums)

print("Part 2:", total)
