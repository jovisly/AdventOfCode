"""
Time: an hour and 40 minutes

Reflections: After first attempting to make a solver for about 20 minutes, I
decided to use z3 instead. I encountered several issues along the way due to my
own unfamiliarity with z3, plus with bitwise operations. The first issue was that
I used Int instead of BitVec -- I've used Int before, e.g., 2022 day 21 part 2,
but that does not work with bitwise operations. Then I kept getting the wrong
answer in part 1, which was extremely puzzling and difficult to debug. I extracted
out the simplest relationship from the dataset: b = 44430 and v = b RSHIFT 1. This
allowed me to see that z3 was giving me a different answer than 44430 >> 1. Reading
the documentation (https://www.cs.tau.ac.il/~msagiv/courses/asv/z3py/guide-examples.htm),
I finally saw that there's a "logical shift right". Switching to that gave me the
right answer finally. Part 2 then took very little time to solve since we just
use the same solver set up.
"""
import z3

def get_dict_instructions(lines):
    # Turn the lines into dictionary of instructions.
    dict_instructions = {}
    for line in lines:
        elements = line.split("->")
        dict_instructions[elements[1].strip()] = elements[0].strip()
    return dict_instructions


def add_instruction(solver, dict_vars, var, instruction, skip_b=False):
    if var == "b" and skip_b:
        return

    if "NOT" in instruction:
        target = instruction.split(" ")[-1]
        if target in dict_vars:
            solver.add(
                dict_vars[var] == ~dict_vars[target]
            )
        else:
            solver.add(
                dict_vars[var] == ~int(target)
            )
    elif "OR" in instruction:
        elements = instruction.split(" OR ")
        elements = [dict_vars[e] if e in dict_vars else int(e) for e in elements]
        solver.add(
            dict_vars[var] == elements[0] | elements[1]
        )
    elif "AND" in instruction:
        elements = instruction.split(" AND ")
        elements = [dict_vars[e] if e in dict_vars else int(e) for e in elements]
        solver.add(
            dict_vars[var] == elements[0] & elements[1]
        )
    elif "LSHIFT" in instruction:
        elements = instruction.split(" LSHIFT ")
        elements = [dict_vars[e] if e in dict_vars else int(e) for e in elements]
        solver.add(
            dict_vars[var] == elements[0] << elements[1]
        )
    elif "RSHIFT" in instruction:
        # https://www.cs.tau.ac.il/~msagiv/courses/asv/z3py/guide-examples.htm
        # Apparently there's a shift right, and there's a "logical shift right".
        elements = instruction.split(" RSHIFT ")
        elements = [dict_vars[e] if e in dict_vars else int(e) for e in elements]
        solver.add(
            # dict_vars[var] == elements[0] >> elements[1]
            dict_vars[var] == z3.LShR(elements[0], elements[1])
        )
    else:
        # In this case, the instruction is either a variable or a number.
        if instruction in dict_vars:
            solver.add(
                dict_vars[var] == dict_vars[instruction]
            )
        else:
            solver.add(
                dict_vars[var] == int(instruction)
            )


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    dict_instructions = get_dict_instructions(lines)

    # Create variables for all the keys.
    dict_vars = {}
    for k in list(dict_instructions):
        dict_vars[k] = z3.BitVec(k, 16)

    solver = z3.Solver()
    for var, instruction in dict_instructions.items():
        add_instruction(solver, dict_vars, var, instruction)

    print("Model check:")
    print(solver.check())
    m = solver.model()
    a = m[dict_vars["a"]].as_long()
    print("Part 1:", a)

    # Reset solver.
    solver = z3.Solver()
    solver.add(dict_vars["b"] == a)
    for var, instruction in dict_instructions.items():
        add_instruction(solver, dict_vars, var, instruction, skip_b=True)

    print("Model check:")
    print(solver.check())
    m = solver.model()
    print("Part 2:", m[dict_vars["a"]].as_long())



if __name__ == "__main__":
    filename = "input.txt"
    solve(filename)


