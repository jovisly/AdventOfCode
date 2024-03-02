# Problem type:
# ~~~~~~~~~~~~ chore ~~~~~~~~~~~~

from collections import defaultdict

filename = "input.txt"

# 1. remove ! and the char after it.
def remove_ex(line):
    newline = line
    while "!" in newline:
        chars = list(newline)
        index = chars.index("!")
        newchars = [c for i, c in enumerate(chars) if i != index and i != index + 1]
        newline = "".join(newchars)
    return newline

assert remove_ex("{{<!!>},{<!!>},{<!!>},{<!!>}}") == "{{<>},{<>},{<>},{<>}}"

# 2. remove garbage
def get_has_gar(line):
    chars = list(line)
    if "<" not in chars:
        return False, None, None

    ind1 = chars.index("<")
    restchars = [c for i, c in enumerate(chars) if i > ind1]
    if ">" not in restchars:
        return False, None, None

    ind2 = chars.index(">")
    return True, ind1, ind2


def remove_gar(line):
    newline = line
    has_gar, ind1, ind2 = get_has_gar(newline)
    while has_gar:
        chars = list(newline)
        newchars = [c for i, c in enumerate(chars) if i < ind1 or i > ind2]
        newline = "".join(newchars)
        has_gar, ind1, ind2 = get_has_gar(newline)
    return newline

assert remove_gar(remove_ex("{{<!!>},{<!!>},{<!!>},{<!!>}}")) == "{{},{},{},{}}"
assert remove_gar(remove_ex("{{<a!>},{<a!>},{<a!>},{<ab>}}")) == "{{}}"

# 3. Tally score
def get_score(line):
    dd = defaultdict(int)
    # Traverse through the line while keeping score.
    curr_depth = 0
    curr_in_bracket = False
    for c in list(line):
        if c == "{":
            curr_depth += 1
        elif c == "}":
            dd[curr_depth] += 1
            curr_depth -= 1
    score = 0
    for k, v in dd.items():
        score += v * k
    return score

assert get_score(remove_gar(remove_ex("{{<a!>},{<a!>},{<a!>},{<ab>}}"))) == 3
assert get_score(remove_gar(remove_ex("{{<!!>},{<!!>},{<!!>},{<!!>}}"))) == 9
assert get_score(remove_gar(remove_ex("{{<ab>},{<ab>},{<ab>},{<ab>}}"))) == 9

lines = open(filename, encoding="utf-8").read().splitlines()
line = lines[0]
line = remove_ex(line)
print("-- done with remove_ex")
line = remove_gar(line)
print("-- done with remove_gar")

print("Part 1:", get_score(line))

# Part 2: need to count garbage size.
def remove_gar_with_count(line):
    newline = line
    has_gar, ind1, ind2 = get_has_gar(newline)
    tot = 0
    while has_gar:
        chars = list(newline)
        newchars = [c for i, c in enumerate(chars) if i < ind1 or i > ind2]
        newline = "".join(newchars)
        tot += ind2 - ind1 - 1
        has_gar, ind1, ind2 = get_has_gar(newline)
    return newline, tot


lines = open(filename, encoding="utf-8").read().splitlines()
line = lines[0]
line = remove_ex(line)
print("-- done with remove_ex")
line, c = remove_gar_with_count(line)
print("-- done with remove_gar_with_count")

# t = '<{o"i!a,<{i<a>'
# t = '<!!!>>'
# t = remove_ex(t)
# b, i1, i2 = get_has_gar(t)
# print(b, i1, i2, i2 - i1 - 1)

print("Part 2:", c, get_score(line))


