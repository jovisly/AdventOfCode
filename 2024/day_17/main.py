"""
Reflections: Huh what is literal vs combo operand?? Mixed them up a lot.
"""
from functools import cache

import utils

filename = "input.txt"
filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().split("\n\n")
registers = lines[0].splitlines()
programs = [int(x) for x in lines[1].split(":")[1].strip().split(",")]


a = int(registers[0].split(": ")[1])
b = int(registers[1].split(": ")[1])
c = int(registers[2].split(": ")[1])


@cache
def get_operand_value(v, a, b, c):
    if v >= 0 and v <= 3:
        return v
    elif v == 4:
        return a
    elif v == 5:
        return b
    elif v == 6:
        return c
    else:
        raise ValueError(f"Unknown operand: {v}")


def do_op(opcode, operand, a, b, c, instruction_pointer):
    out = None
    new_instruction_pointer = None
    if opcode == 0:
        numerator = a
        denominator = 2 ** get_operand_value(operand, a, b, c)
        res = numerator // denominator
        a = res
    elif opcode == 1:
        b = b ^ operand
    elif opcode == 2:
        # If register C contains 9, the program 2,6 would set register B to 1.
        b = get_operand_value(operand, a, b, c) % 8
    elif opcode == 3:
        if a != 0 and operand != instruction_pointer:
            new_instruction_pointer = operand
    elif opcode == 4:
        b = b ^ c
    elif opcode == 5:
        # calculates the value of its combo operand modulo 8, then outputs that value.
        out = get_operand_value(operand, a, b, c) % 8
    elif opcode == 6:
        numerator = a
        denominator = 2 ** get_operand_value(operand, a, b, c)
        res = numerator // denominator
        b = res
    elif opcode == 7:
        numerator = a
        denominator = 2 ** get_operand_value(operand, a, b, c)
        res = numerator // denominator
        c = res
    else:
        raise ValueError(f"Unknown opcode: {opcode}")

    if new_instruction_pointer is None:
        new_instruction_pointer = instruction_pointer + 2
    return out, new_instruction_pointer, a, b, c


instruction_pointer = 0
all_outputs = []
while True:
    opcode = programs[instruction_pointer]
    operand = programs[instruction_pointer + 1]
    out, new_instruction_pointer, a, b, c = do_op(opcode, operand, a, b, c, instruction_pointer)
    instruction_pointer = new_instruction_pointer
    if out is not None:
        all_outputs.append(out)
    if instruction_pointer >= len(programs):
        break

print("Part 1:")
print(",".join(str(x) for x in all_outputs))



"""
Part 2

Reflections: Ooof... Very ad hoc pattern recognition and boundary finding to narrow
down search space. Should really try to figure out how to back track the operations.
"""
filename = "input.txt"
# filename = "input-test2.txt"

lines = open(filename, encoding="utf-8").read().split("\n\n")
registers = lines[0].splitlines()
programs = [int(x) for x in lines[1].split(":")[1].strip().split(",")]

a = int(registers[0].split(": ")[1])
b = int(registers[1].split(": ")[1])
c = int(registers[2].split(": ")[1])

def check_if_copy(a, programs, iter):
    orig_a = a
    b, c, = 0, 0
    programs_str = ",".join(str(x) for x in programs)
    programs_len = len(programs)
    instruction_pointer = 0
    all_outputs = []
    while True or len(all_outputs) >= programs_len:
        opcode = programs[instruction_pointer]
        operand = programs[instruction_pointer + 1]
        out, new_instruction_pointer, a, b, c = do_op(opcode, operand, a, b, c, instruction_pointer)
        instruction_pointer = new_instruction_pointer
        if out is not None:
            all_outputs.append(out)
        if instruction_pointer >= len(programs):
            break
    # program_substr = ",".join(str(x) for x in programs[:len(all_outputs)])
    # if ",".join(str(x) for x in all_outputs) == program_substr:
    #     print(f"a: {a} matches on {program_substr}")
    all_outputs_str = ",".join(str(x) for x in all_outputs)
    # what if we see when the program can produce this many numbers?
    if len(all_outputs) == programs_len and iter % 10000 == 0:
        print(f"a: {orig_a} produces {all_outputs_str}")
    if len(all_outputs) > programs_len and iter % 10000 == 0:
        print("Too many outputs!!", len(all_outputs), programs_len)
    return all_outputs_str == programs_str


# Between 2 ** 44 and 2 ** 48
a = 2 ** 44 + 5
a = 2 ** 47 + 5
a = 2 ** 47 + 2 ** 44 + 5
a = 2 ** 47 + 2 ** 44 + 2 ** 42 + 5
a = 2 ** 47 + 2 ** 44 + 2 ** 42 + 2 ** 41 + 5
a = 2 ** 47 + 2 ** 44 + 2 ** 42 + 2 ** 40 + 2 ** 39 + 2 ** 37 + 5
a = 2 ** 47 + 2 ** 44 + 2 ** 42 + 2 ** 40 + 2 ** 39 + 2 ** 37 + 2 ** 30 + 2 ** 29 + 2 ** 28 + 2 ** 27 + 2 ** 23 + 5
# 2**44:  17592186044416
# 2**48: 281474976710656
# 2 ** 44 * 10 + 6: 2,4,4,4,4,4,4,4,4,4,4,4,4,4,0,1
# 2 ** 45: 4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,4
# 2 ** 46: 4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,6
# 2 ** 47: 4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0
iter = 0
while not check_if_copy(a, programs, iter):
    if iter % 10000 == 0:
        print("Current a:", a)
    a += 2 ** 4
    iter += 1

print("a", a)

# tried: 2**6, 2**8, 2**10, 2**12, 2**16
"""
registers = Registers(a=10, b=0, c=0)
programs = [5, 0, 5, 1, 5, 4]
instruction_pointer = 0
while True:
    opcode = programs[instruction_pointer]
    operand = programs[instruction_pointer + 1]
    out, new_instruction_pointer = do_op(opcode, operand, registers, instruction_pointer)
    instruction_pointer = new_instruction_pointer
    if out is not None:
        print(out)
    if instruction_pointer >= len(programs):
        break
"""

"""
registers = Registers(a=2024, b=0, c=0)
programs = [0, 1, 5, 4,3,0]
instruction_pointer = 0
while True:
    opcode = programs[instruction_pointer]
    operand = programs[instruction_pointer + 1]
    out, new_instruction_pointer = do_op(opcode, operand, registers, instruction_pointer)
    instruction_pointer = new_instruction_pointer
    if out is not None:
        print("out", out)
    if instruction_pointer >= len(programs):
        break
"""

"""
registers = Registers(a=0, b=29, c=0)
programs = [1, 7]
instruction_pointer = 0
while True:
    opcode = programs[instruction_pointer]
    operand = programs[instruction_pointer + 1]
    out, new_instruction_pointer = do_op(opcode, operand, registers, instruction_pointer)
    instruction_pointer = new_instruction_pointer
    if out is not None:
        print("out", out)
    if instruction_pointer >= len(programs):
        break
"""

"""
registers = Registers(a=0, b=2024, c=43690)
programs = [4, 0]
instruction_pointer = 0
while True:
    opcode = programs[instruction_pointer]
    operand = programs[instruction_pointer + 1]
    out, new_instruction_pointer = do_op(opcode, operand, registers, instruction_pointer)
    instruction_pointer = new_instruction_pointer
    if out is not None:
        print("out", out)
    if instruction_pointer >= len(programs):
        break
print(registers)
"""

"""
23_999_685: 5,0,3,5,7,6,1,5,4
20_000_000:
220_364_800_000
"""
