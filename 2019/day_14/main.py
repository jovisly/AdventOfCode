import math
from collections import defaultdict


filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().splitlines()


def process_quantity_and_unit(quantity_and_unit):
    """Given 'number unit', return unit (str), number (int) tuple."""
    components = quantity_and_unit.split(" ")
    quantity = int(components[0].strip())
    unit = components[1].strip()
    return (unit, quantity)


# Ideally we want:
# {(FUEL, 1): {"A": 7, "E": 1}}
def get_product(line):
    components = line.split("=>")
    output = components[1].strip()
    return process_quantity_and_unit(output)


def get_product_name(line):
    components = line.split("=>")
    output = components[1].strip()
    return process_quantity_and_unit(output)[0]


def get_num_products(line):
    components = line.split("=>")
    output = components[1].strip()
    return process_quantity_and_unit(output)[1]


def get_ingredients(line):
    components = line.split("=>")
    inputs = components[0].strip().split(",")
    dict_ingredients = defaultdict(int)
    for i in inputs:
        unit, quantity = process_quantity_and_unit(i.strip())
        dict_ingredients[unit] += quantity
    return dict_ingredients



class Recipe:
    def __init__(self, ingredients, num_products):
        self.ingredients = ingredients
        self.num_products = num_products



dict_recipe = {
    get_product_name(line): Recipe(
        ingredients=get_ingredients(line),
        num_products=get_num_products(line)
    ) for line in lines
}

# print(dict_recipe)

def convert_dict_need(dict_recipe, dict_need, dict_have, item):
    """Convert one of the items in dict_need to its ingredients.

    Side effect: Update dict_need and dict_have. Returns all inputs.
    """
    # print("*** ITEM: ", item)
    # print("   have", dict_have)
    # print("   need", dict_need)
    # 1. identify how many we need
    num_items_needed = dict_need[item]
    if num_items_needed == 0:
        return dict_recipe, dict_need, dict_have

    # 2. identify how many we already have
    if dict_have[item] > 0:
        num_items_to_use = min(num_items_needed, dict_have[item])
        dict_have[item] -= num_items_to_use
        num_items_needed -= num_items_to_use
        dict_need[item] -= num_items_to_use

    if num_items_needed == 0:
        return dict_recipe, dict_need, dict_have

    # 3: get recipe for the item
    recipe = dict_recipe[item]
    ingredients = recipe.ingredients
    num_products = recipe.num_products
    num_rounds = math.ceil(num_items_needed / num_products)

    total_num_products = num_rounds * num_products
    total_num_ingredients = {k: v * num_rounds for k, v in ingredients.items()}

    # 4: Replace dict_need of the item.
    dict_need[item] = 0
    for k, v in total_num_ingredients.items():
        dict_need[k] += v

    # 5. We might have left over
    if total_num_products > num_items_needed:
        dict_have[item] += (total_num_products - num_items_needed)

    # print("   ----")
    # print("   have", dict_have)
    # print("   need", dict_need)

    return dict_recipe, dict_need, dict_have



def get_one_fuel(dict_recipe, dict_have):
    # dict_need = dict_recipe["FUEL"].ingredients.copy()
    dict_need = defaultdict(int)
    for k, v in dict_recipe["FUEL"].ingredients.items():
        dict_need[k] = v

    while True:
        # Pick one of the items in dict_need that is not ORE
        items = [k for k, v in dict_need.items() if v > 0 and k != 'ORE']
        if len(items) == 0:
            return dict_need['ORE'], dict_have

        item = items[0]
        dict_recipe, dict_need, dict_have = convert_dict_need(dict_recipe, dict_need, dict_have, item)


# # Courageously start the process.
# dict_need = dict_recipe["FUEL"].ingredients
# # print(dict_need)
# dict_have = defaultdict(int)

# while True:
#     # Pick one of the items in dict_need that is not ORE
#     items = [k for k, v in dict_need.items() if v > 0 and k != 'ORE']
#     if len(items) == 0:
#         break

#     item = items[0]
#     dict_recipe, dict_need, dict_have = convert_dict_need(dict_recipe, dict_need, dict_have, item)
#     # print("item:", item)


# dict_recipe, dict_need, dict_have = convert_dict_need(dict_recipe, dict_need, dict_have, "A")

# print(dict_need)
# print(dict_have)

# dict_recipe, dict_need, dict_have = convert_dict_need(dict_recipe, dict_need, dict_have, "E")

# print(dict_need)
# print(dict_have)
# dict_have = defaultdict(int)
# num, dict_have = get_one_fuel(dict_recipe, dict_have)

# print("Part 1:", num)

# Part 2 -- 1 trillion ore.
dict_have = defaultdict(int)
tot = 1000000000000
fuel = 0
last_num = 0  # Track the last successful ore usage
while True:
    num, dict_have = get_one_fuel(dict_recipe, dict_have)
    if num > tot:
        break
    last_num = num
    fuel += 1
    tot -= num

print("Part 2:", fuel)
