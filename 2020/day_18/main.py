filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

# Very very simple strategy: find an inner most parenthesis.
def eval_no_paren(expression: str):
    assert "(" not in expression
    assert ")" not in expression

    curr = None
    for char in expression.split(" "):
        # print("." * 20)
        # print(char)
        if char in "+" or char in "*":
            mode = char
            # print(f"  set mode to {char}")
        else:
            if curr is None:
                curr = int(char)
                # print(f"  set curr to {curr}")
            else:
                if mode == "+":
                    curr += int(char)
                if mode == "*":
                    curr *= int(char)
    return curr


# Quick test.
# out = eval_no_paren("1 + 2 * 3 + 4 * 5 + 6")
# print(out)

def find_paren_idx(expression: str):
    # Find idx of inner most, closed parens.
    idx_l = None
    idx_r = None
    for idx, char in enumerate(list(expression)):
        if char == "(":
            idx_l = idx
        if char == ")":
            idx_r = idx
        if idx_l is not None and idx_r is not None:
            return idx_l, idx_r


def eval_expression_in_paren(expression: str):
    assert expression.startswith("(")
    assert expression.endswith(")")
    return eval_no_paren(expression[1:-1])



def eval_and_replace_paren(expression: str):
    assert "(" in expression
    assert ")" in expression
    l, r = find_paren_idx(expression)
    expression_in_paren = expression[l:(r + 1)]
    val = eval_expression_in_paren(expression_in_paren)

    # Now replace the string.
    return expression[:l] + str(val) + expression[(r + 1):]



# Quick tests.
# l, r = find_paren_idx(expression="7 * ((9 + 8 + 9) * 8 + 2) + 5 * 4 * 6")
# print(l, r)

# out = eval_and_replace_paren(expression="7 * ((9 + 8 + 9) * 8 + 2) + 5 * 4 * 6")
# print(out)

def eval_everything(expression: str):
    expression_copy = expression
    while "*" in expression_copy or "+" in expression_copy:
        if "(" in expression_copy and ")" in expression_copy:
            expression_copy = eval_and_replace_paren(expression_copy)
        else:
            val = eval_no_paren(expression_copy)
            return val


# out = eval_everything("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")
# print(out)
s = 0
for line in lines:
    s += eval_everything(line)

print("Part 1:", s)


def eval_and_replace_addition(expression: str):
    assert "+" in expression
    components = expression.split(" ")
    idx = [i for i, c in enumerate(components) if c == "+"][0]
    val = int(components[idx - 1]) + int(components[idx + 1])

    new_arr = components[:idx - 1]
    new_arr.append(str(val))
    new_arr.extend(components[idx + 2:])
    return " ".join(new_arr)

# out = eval_and_replace_addition(expression="6 + 9 * 8 + 6")
# print(out)

# out = eval_and_replace_addition(expression="15 * 8 + 6")
# print(out)

# "+" is evaluated before "*".
def eval_no_paren_part2(expression: str):
    assert "(" not in expression
    assert ")" not in expression

    # Collapse all the "+" until we only have "*".
    copy_expression = expression
    while "+" in copy_expression:
        copy_expression = eval_and_replace_addition(copy_expression)

    # When we dno't have "+" anymore, can just eval normally.
    return eval_no_paren(copy_expression)


def eval_expression_in_paren_part2(expression: str):
    assert expression.startswith("(")
    assert expression.endswith(")")
    return eval_no_paren_part2(expression[1:-1])



def eval_and_replace_paren_part2(expression: str):
    assert "(" in expression
    assert ")" in expression
    l, r = find_paren_idx(expression)
    expression_in_paren = expression[l:(r + 1)]
    val = eval_expression_in_paren_part2(expression_in_paren)

    # Now replace the string.
    return expression[:l] + str(val) + expression[(r + 1):]


def eval_everything_part2(expression: str):
    expression_copy = expression
    while "*" in expression_copy or "+" in expression_copy:
        if "(" in expression_copy and ")" in expression_copy:
            expression_copy = eval_and_replace_paren_part2(expression_copy)
        else:
            val = eval_no_paren_part2(expression_copy)
            return val

# out = eval_everything_part2(expression="((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")
# print(out)
s = 0
for line in lines:
    s += eval_everything_part2(line)

print("Part 2:", s)
