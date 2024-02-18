# Hmm what exactly does "reverse the scrambling process" mean? Just by trial and
# error we know: it's not just by running the instruction in reverse.

# Get the functions that shouldn't change by reversing.
from part1 import swap_position, swap_letter, shift, reverse

START = "fbgdceah"
filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

# Assume this is reversed
lines = lines[::-1]


def get_all_perms(curr):
    perms = []
    for i in range(len(curr)):
        # We are getting all permutations so direction doesn't matter.
        perms.append(shift(curr, i, "right"))
    return perms


# To reverse, "rotate based on position of letter b" requires us to get the index
# of position b. this position has already gotten shifted to the right. but how
# do we determine its previous position? i have no idea but maybe let's generate
# all possibilities and pick the one that matches.
def rotate_based_on(curr, c):
    chars = list(curr)
    i = chars.index(c)
    steps = i + 1
    if i >= 4:
        steps += 1
    return shift(curr, steps, "right")


def rotate_based_on_reversed(curr, instruction):
    c = instruction.split(" ")[-1]
    perms = get_all_perms(curr)
    for perm in perms:
        # Try to rotate based on c and see if we get the current result.
        result = rotate_based_on(perm, c)
        if result == curr:
            return perm

    raise ValueError(f"Cannot identify! {curr}: {instruction}")


# To reverse, "roate left 1 step" should become "rotate right 1 step"
def rotate(curr, instruction):
    segs = instruction.split(" ")
    if segs[1] == "left":
        dir = "right"
    else:
        dir = "left"
    steps = int(segs[2])
    return shift(curr, steps, dir)


# To reverse, "move position x to position y" should be "move position y to position x".
def move(curr, instruction):
    segs = instruction.split(" ")
    ind_next = int(segs[2])
    ind_prev = int(segs[-1])
    chars = list(curr)
    c = chars[ind_prev]
    chars = [c for i, c in enumerate(chars) if i != ind_prev]
    chars = chars[:ind_next] + [c] + chars[ind_next:]
    return "".join(chars)


curr = START
print("curr:", curr)
for line in lines:
    print("... instruction ...", line)
    if line.startswith("swap position"):
        curr = swap_position(curr, line)
    elif line.startswith("swap letter"):
        curr = swap_letter(curr, line)
    elif line.startswith("rotate based on"):
        curr = rotate_based_on_reversed(curr, line)
    elif line.startswith("rotate"):
        curr = rotate(curr, line)
    elif line.startswith("reverse"):
        curr = reverse(curr, line)
    elif line.startswith("move position"):
        curr = move(curr, line)
    else:
        raise ValueError(f"Unknown instruction: {line}")
    print("curr:", curr)


print(curr)
