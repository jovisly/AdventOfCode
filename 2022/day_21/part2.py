"""
Time: 25 minutes.

Reflections: First I tried to extend the methods from part 1, but we need to
trace back. Which will make it a graph problem and we'd need to come up with new
methods anyways. So that took me to z3. This is the third AoC problem I've used
z3 so it's going slightly better in terms of knowing the syntax.

Bug report: It was interesting that the first answer I got from z3 turns out to
be too high. So I added it as another constraint which got me an answer that is
1 minus of the previous answer, which was correct!? I'm quite surprised by this
as I had assumed there'd be only one answer since there's no inequality in the
conditions. Is there some sort of rounding issue? Reading the Reddit thread, I
found out about s.add(a % b == 0). More information is here:
https://www.reddit.com/r/adventofcode/comments/zrult3/2022_day_21_part_2python_solution_with_z3_is_off/
Very interesting...
"""
import z3

def get_monkey_value(line):
    monkey = line.split(":")[0]
    job = line.split(":")[1]
    return monkey, int(job)



def get_job(line):
    m = line.split(":")[0]
    job = line.split(":")[1].strip()
    out = job.split(" ")
    m1 = out[0]
    m2 = out[2]
    operator = out[1]

    return m, m1, m2, operator


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    solver = z3.Solver()

    # First just add all the monkeys.
    dict_vars = {}
    for line in lines:
        monkey = line.split(":")[0]
        dict_vars[monkey] = z3.Int(monkey)

    # Then add the conditions based on each line.
    for line in lines:
        if line.startswith("root:"):
            _, m1, m2, _ = get_job(line)
            solver.add(
                dict_vars[m1] == dict_vars[m2]
            )

        # This is a fake line.
        elif line.startswith("humn:"):
            pass
        elif "+" in line or "-" in line or "*" in line or "/" in line:
            m, m1, m2, operator = get_job(line)
            if operator == "+":
                solver.add(
                    dict_vars[m1] + dict_vars[m2] == dict_vars[m]
                )
            elif operator == "-":
                solver.add(
                    dict_vars[m1] - dict_vars[m2] == dict_vars[m]
                )
            elif operator == "*":
                solver.add(
                    dict_vars[m1] * dict_vars[m2] == dict_vars[m]
                )
            elif operator == "/":
                solver.add(
                    dict_vars[m1] / dict_vars[m2] == dict_vars[m]
                )
                solver.add(
                    dict_vars[m1] % dict_vars[m2] == 0
                )
        else:
            # If we are here, that means the monkey just has a number assignment.
            monkey, value = get_monkey_value(line)
            solver.add(dict_vars[monkey] == value)

    # Had to add this as it was not the right answer (too high).
    # solver.add(dict_vars["humn"] < 3887609741190)
    print("Model check:")
    print(solver.check())
    m = solver.model()

    return m[dict_vars["humn"]].as_long()


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 301


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
    # 3887609741190 is too high.
    # 3887609741189 is right. wow.
