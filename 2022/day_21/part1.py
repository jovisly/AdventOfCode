"""
Time: 10 minutes.

Reflections: Not too bad at all!
"""
def get_monkey(line):
    monkey = line.split(":")[0]
    job = line.split(":")[1]
    if "+" not in job and "-" not in job and "/" not in job and "*" not in job:
        return monkey, int(job)
    else:
        return None, None


def solve_for_monkey(line, dict_monkeys):
    monkey = line.split(":")[0]
    job = line.split(":")[1].strip()
    out = job.split(" ")
    m1 = out[0]
    m2 = out[2]
    operator = out[1]

    if m1 in dict_monkeys and m2 in dict_monkeys:
        v1 = dict_monkeys[m1]
        v2 = dict_monkeys[m2]
        if operator == "+":
            dict_monkeys[monkey] = v1 + v2
        elif operator == "-":
            dict_monkeys[monkey] = v1 - v2
        elif operator == "*":
            dict_monkeys[monkey] = v1 * v2
        elif operator == "/":
            dict_monkeys[monkey] = v1 / v2

        return True, dict_monkeys
    else:
        return False, dict_monkeys



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    dict_monkeys = {}
    remaining_lines = []
    for line in lines:
        monkey, value = get_monkey(line)
        if monkey is not None:
            dict_monkeys[monkey] = value
        else:
            remaining_lines.append(line)


    line = remaining_lines[0]
    while len(remaining_lines) > 0:
        # Try to fill in values of monkeys.
        line = remaining_lines.pop(0)
        success, dict_monkeys = solve_for_monkey(line, dict_monkeys)
        if success == False:
            remaining_lines.append(line)


    return dict_monkeys["root"]


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 152


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
