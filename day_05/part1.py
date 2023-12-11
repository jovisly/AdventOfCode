
def get_seeds(paragraphs):
    str_seeds = paragraphs[0].split(":")[1].strip().split(" ")
    return [int(s) for s in str_seeds]


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


def get_min_location(filename):
    paragraphs = get_paragraphs(filename)
    seeds = get_seeds(paragraphs)

    # Get all the mappings: mappings -> rules -> rule.
    arr_str_mappings = paragraphs[1:]
    arr_mappings = [get_rules(str_mappings) for str_mappings in arr_str_mappings]
    locations = []
    for seed in seeds:
        for rules in arr_mappings:
            seed = apply_rules(seed, rules)
        locations.append(seed)

    return min(locations)



def mini_test():
    filename = "input-test.txt"
    assert get_min_location(filename) == 35


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = get_min_location(filename)

    print(total)


