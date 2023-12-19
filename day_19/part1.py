
def process_input(input):
    """Turn string {x=2036,m=264,a=79,s=2244} into a dictionary."""
    arr_input = input[1:-1].split(",")
    arr_input = [i.split("=") for i in arr_input]
    dict_input = {i[0]: int(i[1]) for i in arr_input}
    return dict_input


def process_rules(rules):
    """Turn string like px{a<2006:qkq,m>2090:A,rfg} into rules.

    Each rule has: a name, an array of operations, where the last operation is
    the "else" statement.
    """
    dict_rules = {}
    for rule in rules:
        rule_name = rule.split("{")[0]
        rule_conditions = rule.split("{")[1][:-1].split(",")
        dict_rules[rule_name] = rule_conditions

    return dict_rules


def apply_result(result):
    """Returns tuple for if to terminate, and what's the result."""
    if result == "A":
        return True, "A"
    elif result == "R":
        return True, "R"
    else:
        return False, result



def apply_condition(condition, input):
    if ">" in condition or "<" in condition:
        result = condition.split(":")[1]
        subject = condition.split(":")[0][0]
        value = int(condition.split(":")[0][2:])
        if ">" in condition and input[subject] > value:
            return apply_result(result)

        if "<" in condition and input[subject] < value:
            return apply_result(result)

        return False, None
    else:
        # No comparison, just the result.
        return apply_result(condition)



def apply_rules(dict_rules, input):
    rule_name = "in"
    terminate = False
    num_steps = 0
    while terminate == False and num_steps <= 15:
        num_steps += 1
        rule = dict_rules[rule_name]
        for condition in rule:
            terminate, result = apply_condition(condition, input)
            if result != None and terminate == False:
                rule_name = result
                break

            if result != None and terminate == True:
                return result



def process_file(filename):
    lines = open(filename, encoding="utf-8").read()
    [rules, inputs] = lines.split("\n\n")
    rules = rules.splitlines()
    inputs = inputs.splitlines()

    dict_rules = process_rules(rules)
    arr_dict_inputs = [process_input(i) for i in inputs]

    return dict_rules, arr_dict_inputs


def solve(filename):
    dict_rules, arr_dict_inputs = process_file(filename)
    arr_accepted = [input for input in arr_dict_inputs if apply_rules(dict_rules, input) == "A"]

    return sum([
        sum(list(input.values()))
        for input in arr_accepted
    ])



def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 19114


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
