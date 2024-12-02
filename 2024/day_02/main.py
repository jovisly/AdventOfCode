"""
Bug report: Forgot to re-calculate the diffs in part 2 after removing an item from the array.
"""
import utils

filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

def is_all_pos(nums):
    return all(n > 0 for n in nums)

def is_all_neg(nums):
    return all(n < 0 for n in nums)

def process_line(line):
    # Get the pairwise diff between each pair of numbers.
    numbers = list(map(int, line.split()))
    diffs = [numbers[i] - numbers[i+1] for i in range(len(numbers) - 1)]

    # Not safe if some are positive and some are negative.
    if not is_all_pos(diffs) and not is_all_neg(diffs):
        return False

    # All numbers need to be abs 1-3.
    if not all(abs(n) in range(1, 4) for n in diffs):
        return False

    return True

res = sum(process_line(line) for line in lines)
print("Part 1:", res)


# Now we can remove one item at a time to check if the remaining is safe.
def get_nums(line):
    numbers = list(map(int, line.split()))
    return numbers


def process_line_2(numbers):
    diffs = [numbers[i] - numbers[i+1] for i in range(len(numbers) - 1)]
    if not is_all_pos(diffs) and not is_all_neg(diffs):
        return False

    # All numbers need to be abs 1-3.
    if not all(abs(n) in range(1, 4) for n in diffs):
        return False

    return True


res = 0
for line in lines:
    nums = get_nums(line)
    # We will try to remove one item at a time.
    for i in range(len(nums)):
        temp_nums = nums[:i] + nums[i+1:]
        if process_line_2(temp_nums):
            res += 1
            break

print("Part 2:", res)


