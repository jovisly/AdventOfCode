"""
Reflections: z3 to find broken instructions which give us an idea how to do the swapping.
"""
import z3
from itertools import combinations

filename = "input.txt"
num_swaps = 4
# filename = "input-test3.txt"
num_swaps = 2
blocks = open(filename, encoding="utf-8").read().split("\n\n")
defs = blocks[0].splitlines()
instructions = blocks[1].splitlines()


def get_key(values):
    """For easier sorting."""
    return int(values[1:])

def get_binary_then_int(dict_values):
    dict_result = dict(sorted(dict_values.items(), reverse=True))
    vals = "".join(str(x) for x in dict_result.values())
    return int(vals, 2)


x_vals = {}
y_vals = {}
for d in defs:
    variable = d.split(": ")[0]
    value = int(d.split(": ")[1])
    if variable.startswith("x"):
        x_vals[get_key(variable)] = value
    elif variable.startswith("y"):
        y_vals[get_key(variable)] = value



x = get_binary_then_int(x_vals)
y = get_binary_then_int(y_vals)

print("x:", x)
print("y:", y)

z = x + y
print("z:", z)

z_bin = bin(z)[2:]
print("z bin:", z_bin, len(z_bin))


z3_solver = z3.Solver()
z3_variables = {}

for d in defs:
    variable = d.split(": ")[0]
    value = int(d.split(": ")[1])
    z3_variables[variable] = z3.BitVec(variable, 1)
    z3_solver.add(z3_variables[variable] == value)


# Also add the conditions from z.
for ind, val in enumerate(list(z_bin)):
    inverse_ind = len(z_bin) - ind - 1
    if inverse_ind < 10:
        variable = f"z0{inverse_ind}"
    else:
        variable = f"z{inverse_ind}"

    z3_variables[variable] = z3.BitVec(variable, 1)
    z3_solver.add(z3_variables[variable] == int(val))

# Sanity check
assert z3_solver.check() == z3.sat

# Now we try to add the instructions and pop the ones that can't sat.
for i in instructions:
    input_operation = i.split(" -> ")[0]
    items = input_operation.split(" ")
    v1 = items[0]
    op = items[1]
    v2 = items[2]
    output = i.split(" -> ")[1]


    if output not in z3_variables:
        z3_variables[output] = z3.BitVec(output, 1)
    if v1 not in z3_variables:
        z3_variables[v1] = z3.BitVec(v1, 1)
    if v2 not in z3_variables:
        z3_variables[v2] = z3.BitVec(v2, 1)


    # Check point.
    z3_solver.push()
    if op == "AND":
        z3_solver.add(z3_variables[output] == z3_variables[v1] & z3_variables[v2])
    elif op == "OR":
        z3_solver.add(z3_variables[output] == z3_variables[v1] | z3_variables[v2])
    elif op == "XOR":
        z3_solver.add(z3_variables[output] == z3_variables[v1] ^ z3_variables[v2])
    else:
        raise ValueError(f"Unknown operation: {op}")

    if z3_solver.check() != z3.sat:
        z3_solver.pop()
        print(f"Instruction {i} can't sat.")
        # Try to see who it can swap with that'd sat?
        for j in instructions:
            output_j = j.split(" -> ")[1]
            if output_j not in z3_variables:
                z3_variables[output_j] = z3.BitVec(output_j, 1)
            z3_solver.push()
            if op == "AND":
                z3_solver.add(z3_variables[output_j] == z3_variables[v1] & z3_variables[v2])
            elif op == "OR":
                z3_solver.add(z3_variables[output_j] == z3_variables[v1] | z3_variables[v2])
            elif op == "XOR":
                z3_solver.add(z3_variables[output_j] == z3_variables[v1] ^ z3_variables[v2])
            if z3_solver.check() == z3.sat:
                # print(f"  - Instruction {j} can sat by switching.")
                pass
            z3_solver.pop()

exit()

"""
This gives us... Not exactly 4 pairs...
Instruction y15 AND x15 -> ksg can't sat.
Instruction x06 AND y06 -> z06 can't sat.
Instruction mjt OR tqm -> svd can't sat.
Instruction sqv AND frp -> z11 can't sat.
Instruction qsv AND tqr -> hmg can't sat.
Instruction mpk AND ctv -> bnb can't sat.
"""

def get_list_instructions(instructions):
    """Get instructions in the form of a list of a list.

    Not that many items so list is fine.
    """
    list_instructions = []
    for i in instructions:
        input_operation = i.split(" -> ")[0]
        items = input_operation.split(" ")
        v1 = items[0]
        op = items[1]
        v2 = items[2]
        output = i.split(" -> ")[1]
        list_instructions.append([v1, op, v2, output])
    return list_instructions


list_instructions = get_list_instructions(instructions)

def get_swapped_instructions(list_instructions, swaps):
    """Get the swapped instructions.

    Swaps is a dictionary of indices to be swapped.
    """
    list_swapped_instructions = []
    for ind, instruction in enumerate(list_instructions):
        if ind in swaps:
            swapped_ind = swaps[ind]
            swapped_instruction = list_instructions[swapped_ind]
            list_swapped_instructions.append([instruction[0], instruction[1], instruction[2], swapped_instruction[3]])
        else:
            list_swapped_instructions.append(instruction)

    return list_swapped_instructions


def find_sln(swaps):
    z3_solver = z3.Solver()
    z3_variables = {}
    for d in defs:
        variable = d.split(": ")[0]
        value = int(d.split(": ")[1])
        z3_variables[variable] = z3.BitVec(variable, 1)
        z3_solver.add(z3_variables[variable] == value)
        if variable.startswith("x"):
            x_vals[get_key(variable)] = value
        elif variable.startswith("y"):
            y_vals[get_key(variable)] = value

    swapped_instructions = get_swapped_instructions(list_instructions, swaps)
    for i in swapped_instructions:
        v1 = i[0]
        op = i[1]
        v2 = i[2]
        output = i[3]

        if output not in z3_variables:
            z3_variables[output] = z3.BitVec(output, 1)
        if v1 not in z3_variables:
            z3_variables[v1] = z3.BitVec(v1, 1)
        if v2 not in z3_variables:
            z3_variables[v2] = z3.BitVec(v2, 1)


        if op == "AND":
            z3_solver.add(z3_variables[output] == z3_variables[v1] & z3_variables[v2])
        elif op == "OR":
            z3_solver.add(z3_variables[output] == z3_variables[v1] | z3_variables[v2])
        elif op == "XOR":
            z3_solver.add(z3_variables[output] == z3_variables[v1] ^ z3_variables[v2])
        else:
            raise ValueError(f"Unknown operation: {op}")

    dict_result = {}
    if z3_solver.check() == z3.sat:
        model = z3_solver.model()
        for v in z3_variables:
            # print(v, model[z3_variables[v]])
            if v.startswith("z"):
                # make the key the int part for easier sorting.
                key = int(v[1:])
                dict_result[key] = model[z3_variables[v]].as_long()
    else:
        print("No solution found!")
        return False


    z = get_binary_then_int(dict_result)
    print("z:", z)
    if x  + y  == z:
        return True
    else:
        return False



# for combo in combinations(range(len(list_instructions)), num_swaps):
#     print(combo)

# find_sln({})



exit()
print(instructions)
exit()
x_vals = {}
y_vals = {}
for d in defs:
    variable = d.split(": ")[0]
    value = int(d.split(": ")[1])
    z3_variables[variable] = z3.BitVec(variable, 1)
    z3_solver.add(z3_variables[variable] == value)
    if variable.startswith("x"):
        x_vals[get_key(variable)] = value
    elif variable.startswith("y"):
        y_vals[get_key(variable)] = value


for i in instructions:
    input_operation = i.split(" -> ")[0]
    items = input_operation.split(" ")
    v1 = items[0]
    op = items[1]
    v2 = items[2]
    output = i.split(" -> ")[1]


    if output not in z3_variables:
        z3_variables[output] = z3.BitVec(output, 1)
    if v1 not in z3_variables:
        z3_variables[v1] = z3.BitVec(v1, 1)
    if v2 not in z3_variables:
        z3_variables[v2] = z3.BitVec(v2, 1)


    if op == "AND":
        z3_solver.add(z3_variables[output] == z3_variables[v1] & z3_variables[v2])
    elif op == "OR":
        z3_solver.add(z3_variables[output] == z3_variables[v1] | z3_variables[v2])
    elif op == "XOR":
        z3_solver.add(z3_variables[output] == z3_variables[v1] ^ z3_variables[v2])
    else:
        raise ValueError(f"Unknown operation: {op}")


dict_result = {}
if z3_solver.check() == z3.sat:
    model = z3_solver.model()
    for v in z3_variables:
        # print(v, model[z3_variables[v]])
        if v.startswith("z"):
            # make the key the int part for easier sorting.
            key = int(v[1:])
            dict_result[key] = model[z3_variables[v]].as_long()
else:
    print("No solution found!")

# Sort the dictinoary by key inverse.
print(get_binary_then_int(dict_result))

print("Part 2:")

