"""
Reflections: z3 z3 z3 z3 z3
"""
import z3

filename = "input.txt"
# filename = "input-test2.txt"
# filename = "input-test1.txt"
# filename = "input-test4.txt"
filename = "input-swapped.txt"
blocks = open(filename, encoding="utf-8").read().split("\n\n")
defs = blocks[0].splitlines()
instructions = blocks[1].splitlines()

z3_solver = z3.Solver()
z3_variables = {}

for d in defs:
    variable = d.split(": ")[0]
    value = int(d.split(": ")[1])
    z3_variables[variable] = z3.BitVec(variable, 1)
    z3_solver.add(z3_variables[variable] == value)


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
dict_result = dict(sorted(dict_result.items(), reverse=True))
# print(dict_result)
vals = "".join(str(x) for x in dict_result.values())
# print(vals)
print("Part 1:", int(vals, 2))
# print(dict_result)
