"""
Reflections: Switched out all the list for tuples. This is not a fast solution though.
We essentially find all the unique diffs and then try all of them. Also optimize so we
don't have to loop back again.
"""
from tqdm import tqdm
from functools import cache

from itertools import product
from collections import defaultdict
from part1 import evolve

filename = "input.txt"
# filename = "input-test2.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

@cache
def get_price(sn):
    return int(str(sn)[-1])

@cache
def get_diffs(prices):
    return tuple([prices[i+1] - prices[i] for i in range(len(prices)-1)])


# Get all the diffs. Also remember, for each secret number, for each diff, what is the price.
dict_all = {}
all_diffs = set()
for n in tqdm(lines):
    dict_diffs_to_price = defaultdict(int)
    sn = int(n)
    prices = tuple([get_price(sn)])
    for _ in range(2000):
        sn = evolve(sn)
        price = get_price(sn)
        prices = prices + (price,)
        # Get the diff from the last 4 + 1 prices.
        if len(prices) >= 5:
            diffs = get_diffs(prices[-5:])
            all_diffs.add(diffs)
            # Only use the first time we see the diff.
            if diffs not in dict_diffs_to_price:
                dict_diffs_to_price[diffs] = price
    dict_all[n] = dict_diffs_to_price

print("Number of unique diffs:", len(all_diffs))

# Now basically try. But we have a dictionary yay!
max_b = 0
max_b_diff = None
for d in tqdm(all_diffs):
    # We can't use the dictinoary which doesn't have ordering information. We sell
    # bananas as soon as we see the diff.
    b = 0
    for n in lines:
        # sn = int(n)
        # b += sell_bananas(sn, d)
        if d in dict_all[n]:
            b += dict_all[n][d]
    if b > max_b:
        max_b = b
        max_b_diff = d


print("Max bananas:", max_b)
print("Max bananas diff:", max_b_diff)

# o = sell_bananas(sn=2024, diffs=[-2,1,-1,3])
# print(o)
# exit()
# All dicts is to keep track of all the different dictionaries.
exit()


def sell_bananas(sn, diffs):
    """Sell bananas as soon as we see the diff."""
    prices = tuple([get_price(sn)])
    for _ in range(2000):
        sn = evolve(sn)
        price = get_price(sn)
        prices = prices + (price,)
        if len(prices) >= 5:
            this_diffs = get_diffs(prices[-5:])
            if diffs == this_diffs:
                # print(prices)
                return price
    # print("COULD NOT SELL THIS BANANAS SOMETHING IS WRONG.")
    return 0


def get_dict_prices_v_diffs(sn):
    # Let's construct a dictionary for prices vs the four consecutive diffs.
    # Defaultdict initialized to a list. Keys should be 0 - 9.
    dict_prices_v_diffs = defaultdict(list)

    prices = [get_price(sn)]
    for _ in range(2000):
        sn = evolve(sn)
        price = get_price(sn)
        prices.append(price)
        # Get the diff from the last 4 + 1 prices.
        if len(prices) >= 5:
            diffs = get_diffs(prices[-5:])
            if diffs not in dict_prices_v_diffs[price]:
                dict_prices_v_diffs[price].append(diffs)
    return dict_prices_v_diffs




all_dicts = {}
for n in tqdm(lines):
    sn = int(n)
    dict_prices_v_diffs = get_dict_prices_v_diffs(sn)
    all_dicts[sn] = dict_prices_v_diffs


keys = []
for dict_prices_v_diffs in all_dicts.values():
    for list_diffs in dict_prices_v_diffs.values():
        for diffs in list_diffs:
            if diffs not in keys:
                keys.append(diffs)

print("Number of unique diffs:", len(keys))
# 6998 not too bad!

# Now basically try.
max_b = 0
max_b_diff = None
for d in tqdm(keys):
    # We can't use the dictinoary which doesn't have ordering information. We sell
    # bananas as soon as we see the diff.
    b = 0
    for n in lines:
        sn = int(n)
        b += sell_bananas(sn, d)
    if b > max_b:
        max_b = b
        max_b_diff = d


print("Max bananas:", max_b)
print("Max bananas diff:", max_b_diff)



exit()
# print(dict_prices_v_diffs)
keys = []
for list_diffs in dict_prices_v_diffs.values():
    for diffs in list_diffs:
        if diffs not in keys:
            keys.append(diffs)

print(len(keys))
# 1924; not bad!



exit()
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -3, -4, -5, -6, -7, -8, -9]
all_combinations = product(digits, repeat=4)

# 16,619,522,798 combinations so it's gonna be slow to try them all.
print(len(list(all_combinations)))

sn = 123
prices = [get_price(sn)]

for _ in range(2000):
    sn = evolve(sn)
    prices.append(get_price(sn))

print(set(get_diffs(prices)))
