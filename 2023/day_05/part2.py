"""Way too slow...

The method here requires going through 2,230,384,402 seeds.
"""
import sys
from tqdm import tqdm

def get_seeds(paragraphs):
    str_seeds = paragraphs[0].split(":")[1].strip().split(" ")
    arr_seed = [int(s) for s in str_seeds]
    # Parse the seeds into tuples of two.
    arr_seed = [(arr_seed[i], arr_seed[i + 1]) for i in range(0, len(arr_seed), 2)]
    return arr_seed


def get_all_seeds(arr_seeds):
    all_seeds = []
    for seed_tuple in tqdm(arr_seeds):
        all_seeds += list(range(seed_tuple[0], seed_tuple[0] + seed_tuple[1]))
    print("Number of seeds:", len(all_seeds))
    return all_seeds


def get_paragraphs(filename):
    with open(filename, 'r') as file:
        all_lines = file.read()

    paragraphs = all_lines.split("\n\n")
    return paragraphs


def get_one_rule(str_rule):
    arr_rule = str_rule.split(" ")
    (a, b, c) = [int(a.strip()) for a in arr_rule]
    return (a, b, c)


def get_rules(input_string):
    """Given a rules string, return list of tuples representing rules.

    Example input: 'soil-to-fertilizer map:\n0 15 37\n37 52 2\n39 0 15'
    Which should return: [(0, 15, 37), ...]
    """
    arr_output = input_string.split(":")[1].split("\n")
    # Throw away non-rules.
    arr_output = [a for a in arr_output if a != ""]
    # For each rule, create an array.
    arr_rules = [get_one_rule(a) for a in arr_output]

    return arr_rules


def apply_one_rule(seed, rule):
    dest, source, length = rule
    delta = source - dest
    mutated = False
    if (seed < source + length and seed >= source):
        seed -= delta
        mutated = True

    return mutated, seed


def apply_rules(seed, rules):
    for rule in rules:
        mutated, seed = apply_one_rule(seed, rule)
        if mutated:
            break

    return seed


def get_min_location(filename, batch_num=None):
    paragraphs = get_paragraphs(filename)
    arr_seeds = get_seeds(paragraphs)
    print(arr_seeds)
    if batch_num is None:
        seeds = get_all_seeds(arr_seeds)
    else:
        seeds = get_all_seeds([arr_seeds[batch_num]])

    # Get all the mappings: mappings -> rules -> rule.
    arr_str_mappings = paragraphs[1:]
    arr_mappings = [get_rules(str_mappings) for str_mappings in arr_str_mappings]
    min_position = float("inf")
    for seed in tqdm(seeds):
        for rules in arr_mappings:
            seed = apply_rules(seed, rules)
        if seed < min_position:
            min_position = seed

    return min_position


def mini_test():
    filename = "input-test.txt"
    assert get_min_location(filename) == 46


if __name__ == "__main__":
    mini_test()

    batch_num = sys.argv[1]
    filename = "input.txt"
    total = get_min_location(filename, int(batch_num))

    print(total)


