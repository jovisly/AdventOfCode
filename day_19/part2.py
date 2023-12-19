import copy
import operator

from part1 import process_rules


def process_file(filename):
    lines = open(filename, encoding="utf-8").read()
    rules = lines.split("\n\n")[0].splitlines()

    dict_rules = process_rules(rules)
    return dict_rules


def get_exception_condition(condition):
    """Given, e.g., 'a>3333', return 'a<=3333'."""
    # print("condition --- ", condition)
    symbol = ">" if ">" in condition else "<"
    exception_symbol = "<=" if ">" in condition else ">="
    subject = condition.split(symbol)[0]
    value = condition.split(symbol)[1]
    return f"{subject}{exception_symbol}{value}"



def traverse_for_a(dict_rules):
    """Find the ways to get to A and construct a good_rules array."""
    queue = [{"curr": "in", "path": []}]
    good_conditions = []

    while len(queue) > 0:
        # print("~~~~~~~")
        # print("queues", queue)
        head = queue.pop(0)
        rules= dict_rules[head["curr"]]
        # print("rule name:", head["curr"])
        # print("rules", rules)

        exception_path = []
        for rule in rules:
            # print("  rule", rule)
            if ">" in rule or "<" in rule:
                condition = rule.split(":")[0]
                result = rule.split(":")[1]
                exception_path.append(get_exception_condition(condition))

                if result == "R":
                    continue
                elif result == "A":
                    head["path"].append(condition)
                    good_conditions.append(head["path"])
                else:
                    # Taking us to a new queue.
                    new_queue = copy.deepcopy(head)
                    new_queue["path"].append(condition)
                    new_queue["curr"] = result
                    queue.append(new_queue)

            else:
                # If we are here, this means the previous conditions need to
                # have failed.
                result = rule
                if result == "R":
                    continue
                elif result == "A":
                    head["path"] += exception_path
                    good_conditions.append(head["path"])
                else:
                    # Create a new queue using exception path.
                    new_queue = copy.deepcopy(head)
                    new_queue["path"] += exception_path
                    new_queue["curr"] = result
                    queue.append(new_queue)

    return good_conditions



def collapse_ranges(ranges):
    ranges.sort(key = operator.itemgetter(0))
    merged_ranges = []
    for r in ranges:
        if not merged_ranges or r[0] > merged_ranges[-1][1]:
            merged_ranges.append(r)
        else:
            merged_ranges[-1][1] = max(merged_ranges[-1][1], r[1])
    return merged_ranges



def count_values_in_ranges(ranges):
    return sum(r[1] - r[0] + 1 for r in ranges)


def parse_good_conditions(good_conditions, rating):
    """Go through the good rules for a rating to find the number of ways."""
    min_rating = 1
    max_rating = 4000
    filtered_good_conditions = [
        [r for r in rule if r.startswith(rating)]
        for rule in good_conditions
    ]
    print("--- filtered ---")
    print(filtered_good_conditions)

    # for each filtered rule, we can apply it to get min and max.
    min_max = []
    for conditions in filtered_good_conditions:
        dict_min_max = {"min": min_rating, "max": max_rating}
        for condition in conditions:
            print("condition:", condition)
            if ">=" in condition:
                value = int(condition.split(">=")[1])
                dict_min_max["min"] = value
            elif "<=" in condition:
                value = int(condition.split("<=")[1])
                dict_min_max["max"] = value
            elif "<" in condition:
                value = int(condition.split("<")[1])
                dict_min_max["max"] = value - 1
            elif ">" in condition:
                value = int(condition.split(">")[1])
                dict_min_max["min"] = value + 1
            else:
                raise ValueError(f"Unknown condition: {condition}")

        if dict_min_max["min"] <= dict_min_max["max"]:
            min_max.append([dict_min_max["min"], dict_min_max["max"]])

    print("--- min_max ---")
    print(min_max)
    collapsed = collapse_ranges(min_max)
    print("--- collapsed ---")
    print(collapsed)
    return count_values_in_ranges(collapsed)




def solve(filename):
    dict_rules = process_file(filename)
    good_conditions = traverse_for_a(dict_rules)
    print("good_conditions:", good_conditions)

    x = parse_good_conditions(good_conditions, "x")
    m = parse_good_conditions(good_conditions, "m")
    a = parse_good_conditions(good_conditions, "a")
    s = parse_good_conditions(good_conditions, "s")
    print("x:", x)
    print("m:", m)
    print("a:", a)
    print("s:", s)
    print("product:", x * m * a * s)
    return 167409079868000


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 167409079868000


if __name__ == "__main__":
    mini_test()

    # filename = "input.txt"
    # total = solve(filename)

    # print(total)
    # Obviously we can't do this.
    # for i in tqdm(range(4000)):
    #     for j in range(4000):
    #         for k in range(4000):
    #             pass
