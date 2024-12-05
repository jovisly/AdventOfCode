"""
Super messy~~~~~~~ For Part 2, tried with all permutations first, but that was way
too slow. Part 2 -- can do proper sorting probably?? But just doing swapping and
that worked...

Extra messy since I have the same functions with different inputs (str vs parsed list).
And all the variable names are messed up.
"""
from tqdm import tqdm
import utils

filename = "input.txt"
# filename = "input-test.txt"
stuff = open(filename, encoding="utf-8").read()
# Split by double newlines.
lines = stuff.split("\n\n")

orders = lines[0].splitlines()
updates = lines[1].splitlines()

# print(orders)
# print(updates)

def is_following_order(order, nums):
    # One order looks like '75|13'
    order_nums = list(map(int, order.split("|")))
    n1 = order_nums[0]
    n2 = order_nums[1]

    # Get the index of n1 and n2 in nums.
    idx1 = next((i for i, x in enumerate(nums) if x == n1), -1)
    idx2 = next((i for i, x in enumerate(nums) if x == n2), -1)

    # Does not matter if either is -1.
    if idx1 == -1 or idx2 == -1:
        return True

    return idx1 < idx2

def check_update(update):
    # One update looks like '97,61,53,29,13'
    nums = list(map(int, update.split(",")))
    # Go through orders and see if they are all abided.
    if all(is_following_order(order, nums) for order in orders):
        return True
    return False

s = 0
for update in updates:
    if check_update(update):
        # Get the middle number.
        nums = list(map(int, update.split(",")))
        middle_idx = len(nums) // 2
        middle_num = nums[middle_idx]
        s += middle_num

print("Part 1:", s)



def check_perm(perm):
    if all(is_following_order(order, perm) for order in orders):
        return True
    return False


unsats = []
for update in updates:
    if not check_update(update):
        # Get the middle number.
        nums = list(map(int, update.split(",")))
        unsats.append(nums)


unsat = unsats[2]

# Would this work lol?
def get_sat(unsat):
    while not check_perm(unsat):
        # Find the first violation and swap.
        for order in orders:
            if not is_following_order(order, unsat):
                # Swap the two numbers in unsat.
                n1, n2 = map(int, order.split("|"))
                unsat[unsat.index(n1)], unsat[unsat.index(n2)] = unsat[unsat.index(n2)], unsat[unsat.index(n1)]
    return unsat

s = 0
for unsat in tqdm(unsats):
    fixed = get_sat(unsat)
    middle_idx = len(fixed) // 2
    s += fixed[middle_idx]


print("Part 2:", s)

exit()

# Can we try all permutations? NOPE -- THIS WILL NOT WORK FOR PART 2.
from itertools import permutations


def check_perm(perm):
    if all(is_following_order(order, perm) for order in orders):
        return True
    return False

unsats = []
for update in updates:
    if not check_update(update):
        # Get the middle number.
        nums = list(map(int, update.split(",")))
        unsats.append(nums)

s = 0
for unsat in tqdm(unsats):
    perms = list(permutations(unsat))
    for perm in perms:
        if check_perm(perm):
            middle_idx = len(perm) // 2
            middle_num = perm[middle_idx]
            s += middle_num
            break


print("Part 2:", s)
