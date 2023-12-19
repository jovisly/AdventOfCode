import copy

from part1 import process_rules


def process_file(filename):
    lines = open(filename, encoding="utf-8").read()
    rules = lines.split("\n\n")[0].splitlines()

    dict_rules = process_rules(rules)
    return dict_rules


def get_exception_condition(condition):
    """Given, e.g., 'a>3333', return 'a<=3333'."""
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
        head = queue.pop(0)
        rules= dict_rules[head["curr"]]

        exception_path = []
        for rule in rules:
            copy_head = copy.deepcopy(head)

            if ">" in rule or "<" in rule:
                condition = rule.split(":")[0]
                result = rule.split(":")[1]

                if result == "R":
                    pass
                elif result == "A":
                    copy_head["path"] += exception_path
                    copy_head["path"].append(condition)
                    good_conditions.append(copy_head["path"])
                else:
                    # Taking us to a new queue.
                    copy_head["path"] += exception_path
                    copy_head["path"].append(condition)
                    copy_head["curr"] = result
                    queue.append(copy_head)

                # If we haven't matched the condition, add it to exception.
                exception_path.append(get_exception_condition(condition))
            else:
                # If we are here, this means the previous conditions need to
                # have failed.
                result = rule
                if result == "R":
                    pass
                elif result == "A":
                    copy_head["path"] += exception_path
                    good_conditions.append(copy_head["path"])
                else:
                    # Create a new queue using exception path.
                    copy_head["path"] += exception_path
                    copy_head["curr"] = result
                    queue.append(copy_head)

    return good_conditions



def parse_good_conditions(conditions):
    """Go through the good rules to find the number of ways."""
    min_rating = 1
    max_rating = 4000

    min_max = {
        c: {"min": min_rating, "max": max_rating}
        for c in list("xmas")
    }

    for c in conditions:
        subject = c[0]
        if ">=" in c:
            value = int(c.split(">=")[1])
            min_max[subject]["min"] = value
        elif "<=" in c:
            value = int(c.split("<=")[1])
            min_max[subject]["max"] = value
        elif "<" in c:
            value = int(c.split("<")[1])
            min_max[subject]["max"] = value - 1
        elif ">" in c:
            value = int(c.split(">")[1])
            min_max[subject]["min"] = value + 1
        else:
            raise ValueError(f"Unknown condition: {c}")

    multiple = 1
    for v in list(min_max.values()):
        multiple *= (v["max"] - v["min"] + 1)

    return multiple




def solve(filename):
    dict_rules = process_file(filename)
    good_conditions = traverse_for_a(dict_rules)

    total = 0
    for conditions in good_conditions:
        # This turned out to work for the test case and even for the actual data
        # set but I'm surprised. Shouldn't we subtract away "overlapped" cases?
        total += parse_good_conditions(conditions)

    return total


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 167409079868000


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
