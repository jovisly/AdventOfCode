import re


def get_replacements(orig, replacement):
    i, o = replacement.split(" => ")

    set_new = set()
    for match in re.finditer(i, orig):
        start, end = match.start(), match.end()
        new = orig[:start] + o + orig[end:]
        set_new.add(new)
    return set_new


def get_all_replacements(curr_str, replacements):
    set_new_all = set()
    for replacement in replacements:
        set_new = get_replacements(curr_str, replacement)
        set_new_all = set_new_all.union(set_new)
    return set_new_all



def solve(filename):
    lines = open(filename, encoding="utf-8").read().split("\n\n")
    replacements = lines[0].splitlines()
    orig = lines[1].strip()
    set_new_all = get_all_replacements(orig, replacements)

    print("Part 1:", len(set_new_all))


if __name__ == "__main__":
    filename = "input.txt"
    solve(filename)



