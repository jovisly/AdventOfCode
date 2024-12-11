"""
Reflections: Fun problem. Part 2 I thought was pattern finding, so got excited to make
a plot, but couldn't find a precise pattern. So tried to make the loop go faster with
a counter and that worked pretty well.
"""
from tqdm import tqdm
import utils

filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

line = lines[0]
# line = "0 1 10 99 999"
# print(line)

nums = [int(n) for n in line.split()]
print(nums)


def blink(num) -> list[int]:
    if num == 0:
        return [1]
    if len(str(num)) % 2 == 0:
        # split the number into two halves, each half is the same length.
        half_len = len(str(num)) // 2
        first_half = str(num)[:half_len]
        second_half = str(num)[half_len:]
        return [int(first_half), int(second_half)]
    else:
        return [num * 2024]

def blink_all(nums) -> list[int]:
    new_nums = []
    for num in nums:
        new_nums.extend(blink(num))
    return new_nums


for _ in tqdm(range(25)):
    nums = blink_all(nums)


print("Part 1:", len(nums))

# We know we will hit slowness but let's get some pattern.
# nums = [int(n) for n in line.split()]
# for i in range(35):
#     nums = blink_all(nums)
#     print(i + 1, ",", len(nums))

# Ok I have no idea what to do with the pattern but I have a spreadsheet haha. What
# if we grow each number individually? The numbers don't affect each other.

from collections import Counter

def blink_count(nums_with_counts):
    new_counts = Counter()
    for num, count in nums_with_counts.items():
        if num == 0:
            new_counts[1] += count
        elif len(str(num)) % 2 == 0:
            # split number
            half_len = len(str(num)) // 2
            first = int(str(num)[:half_len])
            second = int(str(num)[half_len:])
            new_counts[first] += count
            new_counts[second] += count
        else:
            new_counts[num * 2024] += count
    return new_counts


nums = Counter([int(n) for n in line.split()])
# print(nums)
for i in tqdm(range(75)):
    nums = blink_count(nums)
    # print(i + 1, ",", len(nums))


print("Part 2:", sum(nums.values()))
