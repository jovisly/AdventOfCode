START = "abcde"
filename = "input-test.txt"

START = "abcdefgh"
filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

# print(lines)
def swap_position(curr, instruction):
    segs = instruction.split(" ")
    i1 = int(segs[2])
    i2 = int(segs[-1])

    chars = list(curr)
    c1 = chars[i1]
    c2 = chars[i2]
    chars[i1] = c2
    chars[i2] = c1
    return "".join(chars)


def swap_letter(curr, instruction):
    segs = instruction.split(" ")
    c1 = segs[2]
    c2 = segs[-1]

    chars = list(curr)
    i1 = chars.index(c1)
    i2 = chars.index(c2)
    chars[i1] = c2
    chars[i2] = c1
    return "".join(chars)


def shift(curr, steps, dir):
    chars = list(curr)
    for _ in range(steps):
        if dir == "right":
            chars = [chars[-1]] + chars[:-1]
        elif dir == "left":
            chars = chars[1:] + [chars[0]]
        else:
            raise ValueError(f"Invalid direction: {dir}")
    return "".join(chars)



def rotate_based_on(curr, instruction):
    c = instruction.split(" ")[-1]
    chars = list(curr)
    i = chars.index(c)
    steps = i + 1
    if i >= 4:
        steps += 1
    return shift(curr, steps, "right")


def rotate(curr, instruction):
    segs = instruction.split(" ")
    dir = segs[1]
    steps = int(segs[2])
    return shift(curr, steps, dir)


def reverse(curr, instruction):
    segs = instruction.split(" ")
    ind_s = int(segs[2])
    ind_e = int(segs[-1])
    chars = list(curr)
    chars = chars[:ind_s] + chars[ind_s:ind_e + 1][::-1] + chars[ind_e + 1:]
    return "".join(chars)


def move(curr, instruction):
    segs = instruction.split(" ")
    ind_prev = int(segs[2])
    ind_next = int(segs[-1])
    chars = list(curr)
    c = chars[ind_prev]
    chars = [c for i, c in enumerate(chars) if i != ind_prev]
    chars = chars[:ind_next] + [c] + chars[ind_next:]
    return "".join(chars)


if __name__ == "__main__":
    curr = START
    print("curr:", curr)
    for line in lines:
        print("... instruction ...", line)
        if line.startswith("swap position"):
            curr = swap_position(curr, line)
        elif line.startswith("swap letter"):
            curr = swap_letter(curr, line)
        elif line.startswith("rotate based on"):
            curr = rotate_based_on(curr, line)
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
