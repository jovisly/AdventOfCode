x_min = 256310
x_max = 732736


def has_double(n):
    s = str(n)
    for i, c1 in enumerate(list(s)):
        if i == 0:
            continue
        else:
            c0 = list(s)[i - 1]
            if c1 == c0:
                return True
    return False

assert has_double(39817) == False
assert has_double(39917) == True

def never_dec(n):
    s = str(n)
    for i, c1 in enumerate(list(s)):
        if i == 0:
            continue
        else:
            c0 = list(s)[i - 1]
            if c1 < c0:
                return False
    return True

assert never_dec(39817) == False
assert never_dec(39999) == True

n = 0
for x in range(x_min, x_max+1):
    if has_double(x) and never_dec(x):
        n += 1


print("Part 1:", n)


def has_special_double(n):
    s = str(n)
    prev = None
    counts = []
    count = 0
    for c in s:
        # Start the count.
        if c != prev:
            if count > 0:
                counts.append(count)
            count = 1
            prev = c
        else:
            count += 1
    counts.append(count)
    if 2 in counts:
        return True
    else:
        return False

n = 0
for x in range(x_min, x_max+1):
    if has_special_double(x) and never_dec(x):
        n += 1


print("Part 2:", n)
