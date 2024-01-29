"""
Reflections: The question did not specify what to do with jie/jio when the jump
condition was not satisfied. Just sorta guessed that we continue but would've
been nice to spell it out like for hlf, tpl, and inc.
"""

def parse_line(line):
    target = None
    amount = 0
    if line.startswith("hlf"):
        op = "hlf"
        target = line.split(" ")[-1]
    elif line.startswith("tpl"):
        op = "tpl"
        target = line.split(" ")[-1]
    elif line.startswith("inc"):
        op = "inc"
        target = line.split(" ")[-1]
    elif line.startswith("jmp"):
        op = "jmp"
        amount = int(line.split(" ")[-1])
    elif line.startswith("jie"):
        op = "jie"
        target = line.split(",")[0][-1]
        amount = int(line.split(" ")[-1])
    elif line.startswith("jio"):
        op = "jio"
        target = line.split(",")[0][-1]
        amount = int(line.split(" ")[-1])
    else:
        raise ValueError(f"Unexpected format {line}")

    return op, target, amount


def apply_instruction(instruction, a, b, i):
    op, target, amount = instruction
    if op == "hlf":
        i += 1
        if target == "a":
            a = a / 2
        else:
            b = b / 2
    elif op == "tpl":
        i += 1
        if target == "a":
            a = 3 * a
        else:
            b = 3 * b
    elif op == "inc":
        i += 1
        if target == "a":
            a = a + 1
        else:
            b = b + 1
    elif op == "jmp":
        i += amount
    elif op == "jie":
        if target == "a":
            if a % 2 == 0:
                i += amount
            else:
                i += 1
        else:
            if b % 2 == 0:
                i += amount
            else:
                i += 1
    elif op == "jio":
        if target == "a":
            if a == 1:
                i += amount
            else:
                i += 1
        else:
            if b == 1:
                i += amount
            else:
                i += 1

    return a, b, i


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    instructions = [parse_line(line) for line in lines]
    a = 0
    b = 0
    i = 0
    while True:
        # print("=" * 10)
        # print(instructions[i], "a", a, "b", b, "i", i)
        a, b, i = apply_instruction(instructions[i], a, b, i)
        # print("result: ", "a", a, "b", b, "i", i)
        # input()
        if i < 0 or i >= len(instructions):
            break

    print("Part 1:", b)

    a = 1
    b = 0
    i = 0
    while True:
        a, b, i = apply_instruction(instructions[i], a, b, i)
        if i < 0 or i >= len(instructions):
            break
    print("Part 2:", b)



if __name__ == "__main__":
    filename = "input.txt"
    solve(filename)


